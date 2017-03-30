#!/usr/bin/env python

import time
import uuid
import xmlrpclib
import operator
import os
from util.tokenize import Tokenizer
from util.detokenize import Detokenizer
from util.split_sentences import SentenceSplitter
from generalization import Generalization,Function
import apply_bpe


class co():
    pass

class Translator:
    """Handles the 'translate' task for KhresmoiWorker"""

    def __init__(self, translate_port, source_lang, target_lang):
        """Initialize a Translator object according to the given 
        configuration settings."""
        # precompile XML-RPC Moses server addresses
        self.translate_proxy_addr = "http://localhost:" + translate_port + "/RPC2?src="+source_lang+";tgt="+target_lang

        # initialize text processing tools (can be shared among threads)
        self.splitter = SentenceSplitter({'language': source_lang})
        self.tokenizer = Tokenizer({'lowercase': True,
                                    'moses_escape': True})
        self.detokenizer = Detokenizer({'moses_deescape': True,
                                        'capitalize_sents': True,
                                        'language': target_lang})


    def process_task(self, task):
        """Process translation task. Splits request into sentences, then translates and
        recases each sentence."""
        doalign = task.get('alignmentInfo', '').lower() in ['true', 't', 'yes', 'y', '1']
        dodetok = not task.get('detokenize', '').lower() in ['false', 'f', 'no', 'n', '0']
        nbestsize = min(task.get('nBestSize', 1), 10)

        sentences_list = self.splitter.split_sentences(task['text'])
		#sentences_withoutwords_list, words_list = GeneralizeWord(sentence_list,'zh')
        source_list,lexlist,wordslist =Function.sentenceMain(sentences_list,['date','number','email','hyperlink','time'],'zh')		
        # tokenize
        #print source_list,lexlist,wordslist
        src_lines_tok = [self.tokenizer.tokenize(line) for line in source_list]
        src_translate = Generalization.generalize_zh(src_lines_tok,lexlist,wordslist)
        #apply BPE
        codes = co()
        codes.name = '/home/luyi/zh-en-worker-NMT/worker/tasks/code.zh'
        bpe = apply_bpe.BPE(codes, '@@')
        for x in range(0,len(src_translate)):
            src_translate[x] = bpe.segment(src_translate[x]).strip()
        print src_translate[:3]
        #print src_translate
        translated = [self._translate(line, doalign, dodetok, nbestsize) for line in src_translate]
        return _backward_transform({
            'translationId': uuid.uuid4().hex,
            'sentences': translated
        }, doalign, dodetok)

    def _translate(self, src, doalign, dodetok, nbestsize):
        """Translate and recase one sentence. Optionally, word alignment
        between source and target is included in output."""

        # create server proxies (needed for each thread)
        translate_proxy = xmlrpclib.ServerProxy(self.translate_proxy_addr)
       # recase_proxy = xmlrpclib.ServerProxy(self.recase_proxy_addr)



        # translate
        translation = translate_proxy.translate({
            "text": src,
            "align": doalign,
            "nbest": nbestsize,
            "nbest-distinct": True,
        })

        # provide n-best lists
        rank = 0
        hypos = []
        for hypo in translation['nbest']:
            recased = hypo['hyp']
            parsed_hypo = {
                'text': recased,
                'score': hypo['totalScore'],
                'rank': rank,
            }
            if dodetok:
                parsed_hypo['text'] = self.detokenizer.detokenize(recased)

            if doalign:
                parsed_hypo['tokenized'] = recased
                parsed_hypo['alignment-raw'] = _add_tgt_end(hypo['align'], recased)

            rank += 1
            hypos.append(parsed_hypo)

        result = {
            'src': src,
            'translated': hypos,
        }

        if dodetok:
            result['src-tokenized'] = src

        return result

def _add_tgt_end(align, tgttok):
    ks = map(lambda x: x['tgt-start'], align)
    n = len(tgttok.split())
    ks.append(n)
    for i in xrange(len(align)):
        align[i]['tgt-end'] = ks[i + 1] - 1
    return align

def _backward_transform(result, doalign, dodetok):
    """Transform the produced output structure to old format.
    Soon to be deprecated."""
    translation = []
    min_nbest_length = min([len(s['translated']) for s in result['sentences']])
    for rank in range(0, min_nbest_length):
        translated = []
        for sent in result['sentences']:
            oldformat = {}
            if dodetok:
                oldformat['src-tokenized'] = sent['src-tokenized']

            oldformat['text'] = sent['translated'][rank]['text']
            oldformat['rank'] = rank
            oldformat['score'] = sent['translated'][rank]['score']
            if doalign:
                oldformat['tgt-tokenized'] = sent['translated'][rank]['tokenized']
                oldformat['alignment-raw'] = sent['translated'][rank]['alignment-raw']

            translated.append(oldformat)

        translation.append({'translated': translated, 'translationId': result['translationId']})

    return { 'translation': translation }

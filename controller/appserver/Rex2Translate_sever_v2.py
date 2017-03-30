# ecoding=utf-8
import sys;
import re;
import codecs;
import xmlrpc.client;
import requests;
from collections import OrderedDict
import os;
import uuid;
import logging;
from flask import Flask, request, abort, Response, jsonify

# parameters globel
app = Flask(__name__);
zh_en_model_path = './RexModelzhen';
zh_pt_model_path = './RexModelenzh';
en_zh_model_path = './RexModelenzh';
pt_zh_model_path = './RexModelptzh';
zh_pt_re = '';
zh_en_re ='';
en_zh_re ='';
pt_zh_re ='';
reg_dictzh_en_global = OrderedDict();
reg_dicten_zh_global = OrderedDict();
reg_dictzh_pt_global = OrderedDict();
reg_dictpt_zh_global = OrderedDict();
# moses_bin_path='/home/mb55417/tool/mosesdecoder/bin/moses';
# moses_ini_path='/home/mb55417/umcorpus/work/filterIM10/moses.ini';
url = '';
key_tmp = [];

# open readering and writer



Output_tmp = codecs.open('./testingtmp', 'w', encoding='utf-8');


# def function

def GetKeytr(Rexlist, Sentence, Rexdict):
    keysss_tmp = Sentence;
    for word in Rexlist:
            keysss_tmp = keysss_tmp.replace(word, '(.*)');
    return Rexdict[keysss_tmp];


def RegularModel(rexlist, inputfile):
    RegularModel_File = codecs.open(inputfile, 'r', encoding='utf-8');
    i = 0;
    pattern = re.compile(r'MZslot[0-9]');
    this_list = []
    while True:
        reg_reader_byline = RegularModel_File.readline().strip();
        if reg_reader_byline == '':
            break;
        i += 1;
        link1 = reg_reader_byline.replace('(', '\(').replace(')', '\)').replace('.', '\.').replace('*',
                                                                                                   '\*').replace(
            '?', '\?').replace('!', '\!').replace('|', '\|').replace('+', '\+').replace('[', '\[').replace(']',
                                                                                                           '\]').replace(
            '"', '\"').replace('%', '\%').replace('&', '\&').replace('-', '\-').replace('#', '\#').replace('@',
                                                                                                           '\@').replace(
            '^', '\^').replace('\'', '\'').replace('{', '\{').replace('}', '\}').replace('<',
                                                                                         '\<').replace(
            '>', '\>');

        link = re.sub(pattern, '(.*)', link1);
        this_list.append(link)
        # rex+=reg_reader_byline+'|';
        translation_tmp = RegularModel_File.readline().strip();
        # link = re.sub(re.compile(r'n.º MZslot[0-9]'), '(n.º.*)', reg_reader_byline); # replace 'n.º slotX' to 'n.º XXX'
        rexlist[re.sub(pattern, '(.*)', reg_reader_byline)] = translation_tmp;
        if i % 100000 == 0:
            print(i)

            # print(link)
    Rextest = '|'.join(this_list)
    RegularModel_File.close();
    return Rextest


def CallController(translatelist, sLang, tLang):
    list_translated = [];
    for i in range(len(translatelist)):
        payload = {'sourceLang': sLang, 'targetLang': tLang, 'text': translatelist[i]}
        r = requests.get('http://10.119.31.33:8200/controller', params=payload)

        data = r.json();

        result = data['translation'][0]['translated'][0]['text']
        list_translated.append(result);
    return list_translated;


def chineseSegmentation(test):
    payload = {'key': test, 'format': 'simple'}
    r = requests.get('http://10.119.181.194:11200', params=payload)
    return (r.text);



def Replace_self(translation_list, sentence):
    link = sentence;

    for i in range(len(translation_list)):
        reg_tmp = 'MZslot' + str(i);

        pattern1 = re.compile(r'' + reg_tmp + '');
        # print(reg_dict_global[regular_param]);
        link = re.sub(pattern1, translation_list[i], link);
    return link


# post tag=text
dict = OrderedDict();


@app.route('/translation', methods=['POST'])
def start():
    # if have post text
    if request.method == 'POST':

        input_string = request.form['text'].strip();
        source_lang = request.form['sourceLang'];
        target_lang = request.form['targetLang'];


        if source_lang == 'zh' and target_lang == 'en':
            dict = reg_dictzh_en_global;
            input_string = input_string.replace(' ', '');

        elif source_lang == 'en' and target_lang == 'zh':
            dict = reg_dicten_zh_global;

        elif source_lang == 'zh' and target_lang == 'pt':
            dict = reg_dictzh_pt_global;
            input_string = input_string.replace(' ', '');
            regla_tmp = zh_pt_re;
        else:
            dict = reg_dictpt_zh_global;

        # print(len(key_tmp));
        pattern_tmep = '';
        f = re.findall(regla_tmp,input_string);

        list = [];
        for word in f:
            for i in word:
                if i != '':
                    list.append(i);

        if f :
            trans_tmp = Replace_self(CallController(list, source_lang, target_lang), GetKeytr(list,input_string,dict) );
            print(GetKeytr(list,input_string,dict))
            result = '{\"errorCode\": 0, \"translation\": [{\"translated\": [{\"alignment-raw\":\"[]\",\"src-tokenized\":\"' + str(
                input_string).replace(r'\n',
                                      '') + '\",\"tgt-tokenized\":\"' + trans_tmp + '\", \"score\": \"0\", \"rank\": \"0\", \"text\":\"' + trans_tmp + '\"}],\"translationId\":\"' + uuid.uuid4().hex + '\"}], \"errorMessage\": \"OK\"}'

            return str(trans_tmp);
        else:
            return 'False';



if __name__ == "__main__":
    zh_en_re = re.compile(RegularModel(reg_dictzh_en_global, zh_en_model_path));
    en_zh_re = re.compile(RegularModel(reg_dicten_zh_global, en_zh_model_path));
    zh_pt_re = re.compile(RegularModel(reg_dictzh_pt_global, zh_pt_model_path));
    pt_zh_re = re.compile(RegularModel(reg_dictpt_zh_global, pt_zh_model_path));
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(message)s")
    logger = logging.getLogger('server')
    app.run(host="", port=8080);

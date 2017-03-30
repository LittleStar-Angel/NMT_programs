# -*- coding: utf-8 -*-
import Generalization,Function
src_lines=["鼎盛旅游服务有限公司".decode('utf8')]
source_list,lexlist,wordlist=Function.sentenceMain(src_lines,['date','number','email','hyperlink','time'],'zh')		
print source_list
print lexlist
print wordlist
#src_lines_tok = [self.tokenizer.tokenize(line) for line in source_list]
src_translate = Generalization.generalize_zh(source_list,lexlist,wordlist)
print src_translate
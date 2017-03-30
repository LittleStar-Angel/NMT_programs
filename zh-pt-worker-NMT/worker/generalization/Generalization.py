#encoding=utf-8

# The Program is used to replace the word which is match to the Regular Expression in the corpus
#----------------------------------------------------------------------------------------------
# Begin Program
import re
import os
import sys
import time
from RE_Base import get_LanguageType, get_PatternType
from File_Function import cut_f, del_parts_f, merge_f
from Function import SinMain, SinDicMain, BiMain, BiDicMain,sentenceMain
from subprocess import call
from optparse import OptionParser
from multiprocessing import Pool


def replace(line,list,type):
	import re
	keyword ='d'+type+'b'
	match = re.finditer(keyword, line)
	i=0
	for word in match:
		if i==len(list):break
		source,target = list[i]
		if source==None and target==None: continue
		#print source,target
		#print target
		if source!=None and target==None:
			line = re.sub(keyword, source.decode('utf8').lstrip().rstrip(), line, count = 1)
			line = re.sub("  ", " ", line)
			i += 1
			continue
		xmlstring = '<'+type+ ' translation=\"'+target.decode('utf8').lstrip().rstrip()+'\">'+source.decode('utf8').lstrip().rstrip()+'</'+type+'> '
		line = re.sub(keyword, xmlstring, line, count = 1)
		line = re.sub("  ", " ", line)	
		i += 1
	return line
# Call Replacement Main Function
##########################################################################################
			#SinMain(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, options.singleLanguage, options.multiprocessing, 0)
			
def generalize_zh(src_lines,lexlist,words):
	import date_translate as DT
	import time_translate as TT
	import num_translate as NT
	#import words_translate as WT
	date,time,num,web,email=[],[],[],[],[]
	sentences = []
	for line in lexlist:
		if line[1] == 0:
			date.append((line[0],DT.date_translate(line[0],'pt')))
		elif line[1] == 1:
			time.append((line[0],TT.time_translate(line[0],'pt')))
		elif line[1] == 2:
			email.append((line[0],line[0]))
		elif line[1] == 3:
			web.append((line[0],line[0]))
		elif line[1] == 4:
			num.append((line[0],NT.num_translate(line[0],'pt')))
	for sentence in src_lines:
		sentence = replace(sentence,words,'words')
		sentence = replace(sentence,time,'time')	
		sentence = replace(sentence,date,'date')
		sentence = replace(sentence,num,'num')	
		sentence = replace(sentence,email,'email')
		sentence = replace(sentence,web,'hyperlink')
		sentences.append(sentence)
	return sentences
			
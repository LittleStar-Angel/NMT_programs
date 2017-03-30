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
from Function import SinMain, SinDicMain, BiMain, BiDicMain
from subprocess import call
from optparse import OptionParser
from multiprocessing import Pool



start_time = time.time()

Patter_path = os.path.abspath(__file__)

# Parameter setting
##########################################################################################
Usage = 'usage: python %prog -i filename [Other options]'

# set the attribute of the option
parser = OptionParser(usage = Usage)
parser.add_option('-i', '--filename', dest = 'filename', help = 'The program will find the FILENAME.en and FILENAME.zh, then output FILENAME.pat.en, FILENAME.pat.zh and FILENAME.en-zh.')
parser.add_option('-o', '--outputFilename', dest = 'outputFilename', help = 'output OUTPUTFILENAME.pat.en, OUTPUTFILENAME.pat.zh and OUTPUTFILENAME.en-zh.')
parser.add_option('-l', '--bilexiconFilename', dest = 'bilexiconFilename', help = 'output BILEXICONFILENAME.en-zh')
parser.add_option('-m', '--bilexiconFormat',action = 'store_true', dest = 'bilexiconFormat', default = False, help = 'if -m is given, alternative format output OUTPUTFILENAME.m.en-zh.')
parser.add_option('-s', '--singleLanguage', dest = 'singleLanguage', help = 'enter only ouput single language(en or zh) **Cannot use with -b together')
parser.add_option('-b', '--bilexicon', dest = 'two_Language', help = 'enter two language type. ex: -b en/zh \(if do not use this option, it will defualt to zh, en\) (Type: en, zh, pt) **Cannot use with -s together')
parser.add_option('-v', '--option', dest = 'option', help = 'enter 0/1/2 for different bilexiconFormat Option and the output will be OUTPUTFILENAME.v0/1/2.en-zh')
parser.add_option('-p', '--patternizedSentence', dest = 'no_pattern', help = 'output 4 more files: outputFilename.p.en, outputFilename.p.zh, outputFilename.u.en, outputFilename.u.zh. *no_pattern means the number of patterns that the line have, then print the line in p file, else print in u file. If have not limit, please input \'n\'.')
parser.add_option('-t', '--patternType', dest = 'pType', help = 'Enter the type of pattern you want to replace. (ex: -t date/time ) Now the Program provide [date, time, email, hyperlink, number]')
parser.add_option('-d', '--dictionary', dest = 'dictionary', default = False, action = 'store_true', help = 'use dictionary to help finding pattern.')
parser.add_option('-n', '--noNone', dest = 'nononemode', default = False, action ='store_true', help = 'Use this option to omit the pattern which cannot find another pattern to alignment in bilexicon mode')
parser.add_option('-f','--multiprocessing', dest = 'multiprocessing', help = 'Processing by using multiprocessing. (ex: -f num_of_process)')

(options, args) = parser.parse_args()



# Declaration of some global variables
##########################################################################################
infilename = str()
outfilename = str()
otfilename = str()

Type = get_PatternType()
L_Type = get_LanguageType()



# Filename setting and user input checking
##########################################################################################
if options.filename:
	infilename = options.filename
	outfilename = options.filename
	otfilename = options.filename
else:
	print '**Please input ( -i filename )'
	call(['python', Patter_path, '-h'])
	quit()
	
if options.outputFilename:
	outfilename = options.outputFilename
	otfilename = options.outputFilename

if options.bilexiconFilename:
	otfilename = options.bilexiconFilename

if options.bilexiconFormat:
	otfilename = otfilename + '.m'

if options.option:
	if options.option not in ['0','1','2']:
		print '**Option must be: 0/1/2'
		call(['python', Patter_path, '-h'])
		quit()
	else:
		otfilename = otfilename + '.v' + options.option

pTypel = None
if options.pType:
	pTypel = options.pType.split('/')
	for t in pTypel:
		if t not in Type.keys():
			print '**Pattern type must be',
			print Type.keys()
			call(['python', Patter_path, '-h'])
			quit()
			
if options.nononemode:
	if options.singleLanguage:
		print '**No None mode cannot use in single language mode.'
		call(['python', Patter_path, '-h'])
		quit()
			
if options.multiprocessing:
	try:
		num_threads = int(options.multiprocessing)
	except:
		print '**Num of multiprocessing must be integer.'
		call(['python', Patter_path, '-h'])
		quit()
	
	if num_threads > 10:
		print '**Num of multiprocessing must be in [1,10]'
		call(['python', Patter_path, '-h'])
		quit()

if options.two_Language and options.singleLanguage:
	print "**Option \'-b\' and \'-s\' cannot use together."
	call(['python', Patter_path, '-h'])
	quit()
		
if options.two_Language:
	two_lan = options.two_Language.split('/')
	
	if len(two_lan) != 2:
		print "**Input Error: option \'-b\' input error (example: -b en/zh)"
		call(['python', Patter_path, '-h'])
		quit()
		
	if two_lan[0] not in L_Type or two_lan[1] not in L_Type:
		print "**Input Error: option \'-b\', Not support language type are inputed."
		call(['python', Patter_path, '-h'])
		quit()
	

# Call Replacement Main Function
##########################################################################################
if options.multiprocessing:
	p = Pool()
	
	if options.singleLanguage:
		try:
			f = open(infilename + '.' + options.singleLanguage)
			f.close()
		except:
			print '**File \'%s.' % infilename + sLanguage + '.' + multiprocessing + '\' is not exist.'
			call(['python', Patter_path, '-h'])
			quit()
		
		lines_per_part = cut_f(infilename + '.' + options.singleLanguage, num_threads)
		
		if options.dictionary:
			for i in range(1,num_threads+1):
				p.apply_async(SinDicMain, args=(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, options.singleLanguage, str(i), lines_per_part))
		else:
			for i in range(1,num_threads+1):
				p.apply_async(SinMain, args=(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, options.singleLanguage, str(i), lines_per_part))
				
		print 'Waiting for all subprocess done...'
		p.close()
		p.join()
		print 'All subprocesses done.'
		
		merge_f(outfilename + '.pat.' + options.singleLanguage, num_threads)
		del_parts_f(outfilename + '.pat.' + options.singleLanguage, num_threads)
		merge_f(otfilename + '.lex.' + options.singleLanguage, num_threads)
		del_parts_f(otfilename + '.lex.' + options.singleLanguage, num_threads)
		if options.no_pattern:
			merge_f(outfilename + '.p.' + options.singleLanguage, num_threads)
			del_parts_f(outfilename + '.p.' + options.singleLanguage, num_threads)
			merge_f(outfilename + '.u.' + options.singleLanguage, num_threads)
			del_parts_f(outfilename + '.u.' + options.singleLanguage, num_threads)
			
		del_parts_f(infilename + '.' + options.singleLanguage, num_threads)
	else:
		if options.two_Language:
			olanguage = two_lan[0]
			tlanguage = two_lan[1]
		else:
			olanguage = 'en'
			tlanguage = 'zh'
		
		try:
			f = open(infilename + '.' + olanguage)
			f.close()
			f = open(infilename + '.' + tlanguage)
			f.close()
		except:
			print '**File \'%s.en\' or \'%s.zh\' is not exist.' % (infilename, infilename)
			call(['python', Patter_path, '-h'])
			quit()
		
		# Cut file to be part
		lines_per_part = cut_f(infilename + '.' + olanguage, num_threads)
		lines_per_part = cut_f(infilename + '.' + tlanguage, num_threads)
		
		if options.dictionary:
			for i in range(1,num_threads+1):
				p.apply_async(BiDicMain, args=(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, olanguage, tlanguage, options.nononemode, str(i), lines_per_part))
		else:
			for i in range(1,num_threads+1):
				p.apply_async(BiMain, args=(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, olanguage, tlanguage, options.nononemode, str(i), lines_per_part))
		
		print 'Waiting for all subprocess done...'
		p.close()
		p.join()
		print 'All subprocesses done.'
		
		merge_f(outfilename + '.pat.' + olanguage, num_threads)
		del_parts_f(outfilename + '.pat.' + olanguage, num_threads)
		merge_f(outfilename + '.pat.' + tlanguage, num_threads)
		del_parts_f(outfilename + '.pat.' + tlanguage, num_threads)
		merge_f(otfilename + '.' + olanguage + '-' + tlanguage, num_threads)
		del_parts_f(otfilename + '.' + olanguage + '-' + tlanguage, num_threads)
		if options.no_pattern:
			merge_f(outfilename + '.p.' + olanguage, num_threads)
			del_parts_f(outfilename + '.p.' + olanguage, num_threads)
			merge_f(outfilename + '.u.' + olanguage, num_threads)
			del_parts_f(outfilename + '.u.' + olanguage, num_threads)
			merge_f(outfilename + '.p.' + tlanguage, num_threads)
			del_parts_f(outfilename + '.p.' + tlanguage, num_threads)
			merge_f(outfilename + '.u.' + tlanguage, num_threads)
			del_parts_f(outfilename + '.u.' + tlanguage, num_threads)
			
		del_parts_f(infilename + '.' + olanguage, num_threads)
		del_parts_f(infilename + '.' + tlanguage, num_threads)
else:
	if options.singleLanguage:
		if options.dictionary:
			SinDicMain(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, options.singleLanguage, options.multiprocessing, 0)
		else:
			SinMain(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, options.singleLanguage, options.multiprocessing, 0)
	else:
		if options.two_Language:
			olanguage = two_lan[0]
			tlanguage = two_lan[1]
		else:
			olanguage = 'en'
			tlanguage = 'zh'
		
		if options.dictionary:
			BiDicMain(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, olanguage, tlanguage, options.nononemode, options.multiprocessing, 0)
		else:
			BiMain(infilename, outfilename, otfilename, options.no_pattern, options.bilexiconFormat, options.option, pTypel, olanguage, tlanguage, options.nononemode, options.multiprocessing, 0)



# Count the processing time
##########################################################################################
print("Execution time: %s seconds " % (time.time()-start_time))

# End Program
#----------------------------------------------------------------------------------------------

#encoding=utf8

import sys
import re
import os
from RE_Base import get_RE, get_LanguageType, get_PatternType, get_Symbol
from Trie_Tree import find_word
from subprocess import call

Patter_path = os.path.abspath(__file__)

Bi_olan = str()
Bi_tlan = str()

# convert english number to digit--------------------------------------------------------------
##################################################
def en_di(en):
	en = en.lower()
	en = re.sub(',','',en)
	en = re.sub('-',' ',en)
	en = en.split(' ')
	digit = 0

	en_di_dic = {}
	en_di_dic.setdefault('a',1)
	en_di_dic.setdefault('one',1)
	en_di_dic.setdefault('two',2)
	en_di_dic.setdefault('three',3)
	en_di_dic.setdefault('four',4)
	en_di_dic.setdefault('five',5)
	en_di_dic.setdefault('six',6)
	en_di_dic.setdefault('seven',7)
	en_di_dic.setdefault('eight',8)
	en_di_dic.setdefault('nine',9)
	en_di_dic.setdefault('ten',10)
	en_di_dic.setdefault('eleven',11)
	en_di_dic.setdefault('twelve',12)
	en_di_dic.setdefault('thirteen',13)
	en_di_dic.setdefault('fourteen',14)
	en_di_dic.setdefault('fifteen',15)
	en_di_dic.setdefault('sixteen',16)
	en_di_dic.setdefault('seventeen',17)
	en_di_dic.setdefault('eighteen',18)
	en_di_dic.setdefault('nineteen',19)
	en_di_dic.setdefault('twenty',20)
	en_di_dic.setdefault('thirty',30)
	en_di_dic.setdefault('forty',40)
	en_di_dic.setdefault('fifty',50)
	en_di_dic.setdefault('sixty',60)
	en_di_dic.setdefault('seventy',70)
	en_di_dic.setdefault('eighty',80)
	en_di_dic.setdefault('ninety',90)
	en_di_dic.setdefault('hundred',100)
	en_di_dic.setdefault('thousand',1000)
	en_di_dic.setdefault('million',1000000)
	en_di_dic.setdefault('billion',1000000000)
	en_di_dic.setdefault('trillion',1000000000000)
	en_di_dic.setdefault('first',1)
	en_di_dic.setdefault('second',2)
	en_di_dic.setdefault('third',3)
	en_di_dic.setdefault('fourth',4)
	en_di_dic.setdefault('fifth',5)
	en_di_dic.setdefault('sixth',6)
	en_di_dic.setdefault('seventh',7)
	en_di_dic.setdefault('eighth',8)
	en_di_dic.setdefault('ninth',9)
	en_di_dic.setdefault('tenth',10)
	RE_b = '\\b(a|one|two|three|four|five|six|seven|eight|nine|first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth)\\b'
	RE_t = '\\b(ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)\\b'
	RE_h = '\\b(hundred)'
	RE_o = '\\b(thousand|million|billion|trillion)'

	digit = 0
	num = 0
	hundit = True

	for i in en:
		ContinueSignal = False

		match = re.finditer(RE_b, i)
		for word in match:
			num = num + en_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue
			
		match = re.finditer(RE_t, i)
		for word in match:
			num = num + en_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue

		match = re.finditer(RE_h, i)
		for word in match:
			num = num * en_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue

		match = re.finditer(RE_o, i)
		for word in match:
			num = num * en_di_dic[word.group()]
			digit = digit + num
			num = 0
			ContinueSignal = True
		if ContinueSignal:
			continue

		try:
			num = num + float(i)
		except:
			continue

	digit = digit + num

	if digit % 1 == 0:
		return str(int(digit))
	else:
		return str(digit)

# convert PT number to digit--------------------------------------------------------------
##################################################
def pt_di(pt):
	pt = pt.lower()
	pt = re.sub(',','',pt)
	pt = re.sub('-',' ',pt)
	pt = re.sub('n.º ','',pt)
	pt = re.sub('/','',pt)
	pt = re.sub('.º','',pt)
	pt = re.sub('.ª','',pt)
	pt = re.sub(' ','',pt)	
	pt = pt.split(' ')
	digit = 0

	pt_di_dic = {}
	pt_di_dic.setdefault('um',1)
	pt_di_dic.setdefault('uma',1)
	pt_di_dic.setdefault('dois',2)
	pt_di_dic.setdefault('duas',2)	
	pt_di_dic.setdefault('três',3)
	pt_di_dic.setdefault('quatro',4)
	pt_di_dic.setdefault('cinco',5)
	pt_di_dic.setdefault('seis',6)
	pt_di_dic.setdefault('sete',7)
	pt_di_dic.setdefault('oito',8)
	pt_di_dic.setdefault('nove',9)
	pt_di_dic.setdefault('dez',10)
	pt_di_dic.setdefault('onze',11)
	pt_di_dic.setdefault('doze',12)
	pt_di_dic.setdefault('treze',13)
	pt_di_dic.setdefault('catorze',14)
	pt_di_dic.setdefault('quinze',15)
	pt_di_dic.setdefault('dezasseis',16)
	pt_di_dic.setdefault('dezassete',17)
	pt_di_dic.setdefault('dezoito',18)
	pt_di_dic.setdefault('dezanove',19)
	pt_di_dic.setdefault('vinte',20)
	pt_di_dic.setdefault('trinta',30)
	pt_di_dic.setdefault('quarenta',40)
	pt_di_dic.setdefault('cinquenta',50)
	pt_di_dic.setdefault('sessenta',60)
	pt_di_dic.setdefault('setenta',70)
	pt_di_dic.setdefault('oitenta',80)
	pt_di_dic.setdefault('noventa',90)
	pt_di_dic.setdefault('cem',100)
	pt_di_dic.setdefault('cento',100)
	pt_di_dic.setdefault('mil',1000)
	pt_di_dic.setdefault('dez mil',10000)
	pt_di_dic.setdefault('cem mil',100000)
	pt_di_dic.setdefault('um milhão',1000000)
	pt_di_dic.setdefault('um bilião',1000000000)	
	pt_di_dic.setdefault('primeiro',1)
	pt_di_dic.setdefault('segundo',2)
	pt_di_dic.setdefault('terceiro',3)
	pt_di_dic.setdefault('quarto',4)
	pt_di_dic.setdefault('quinto',5)
	pt_di_dic.setdefault('sexto',6)
	pt_di_dic.setdefault('sétimo',7)
	pt_di_dic.setdefault('oitavo',8)
	pt_di_dic.setdefault('nono',9)
	pt_di_dic.setdefault('décimo',10)
	RE_b = '\\b(um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|primeiro|segundo|terceiro|quarto|quinto|sexto|sétimo|oitavo|nono|décimo)\\b'
	RE_t = '\\b(dez|onze|doze|treze|catorze|quinze|dezasseis|dezassete|dezoito|dezanove|vinte|trinta|quarenta|cinquenta|sessenta|setenta|oitenta|noventa)\\b'
	RE_h = '\\b(cem|cento)'
	RE_o = '\\b(cem mil|dez mil|mil|um milhão|um bilião)'

	digit = 0
	num = 0
	hundit = True

	for i in pt:
		ContinueSignal = False

		match = re.finditer(RE_b, i)
		for word in match:
			num = num + pt_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue
			
		match = re.finditer(RE_t, i)
		for word in match:
			num = num + pt_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue

		match = re.finditer(RE_h, i)
		for word in match:
			num = num * pt_di_dic[word.group()]
			ContinueSignal = True
		if ContinueSignal:
			continue

		match = re.finditer(RE_o, i)
		for word in match:
			num = num * pt_di_dic[word.group()]
			digit = digit + num
			num = 0
			ContinueSignal = True
		if ContinueSignal:
			continue

		try:
			num = num + float(i)
		except:
			continue

	digit = digit + num

	if digit % 1 == 0:
		return str(int(digit))
	else:
		return str(digit)


# token the chinese number, output to list-------------------------------------------------
##################################################
def ch_num_token(s):
	dlist = ['0','1','2','3','4','5','6','7','8','9','.']
	
	s = s.decode('utf8')

	sl = []

	s1 = ''

	for i in s:
		if i in dlist:
			s1 = s1 + i
		else:
			if s1 == '':
				sl.append(i)
			else:
				sl.append(s1)
				sl.append(i)
				s1 = ''

	if s1 != '':
		sl.append(s1)

	return sl




# convert chinese number to digit-------------------------------------------------------
##################################################
def zh_di(ch):
	ch = re.sub(',','',ch)
	ch = re.sub('，','',ch)
	ch = re.sub('．','.',ch)
	ch = re.sub('第','',ch)
	ch = re.sub('/','',ch)
	ch = re.sub('號','',ch)	
	ch = re.sub('等','',ch)
	ch = re.sub('０','0',ch)
	ch = re.sub('１','1',ch)
	ch = re.sub('２','2',ch)
	ch = re.sub('３','3',ch)
	ch = re.sub('４','4',ch)
	ch = re.sub('５','5',ch)
	ch = re.sub('６','6',ch)
	ch = re.sub('７','7',ch)
	ch = re.sub('８','8',ch)
	ch = re.sub('９','9',ch)
	ch = re.sub('点','.',ch)
	ch = re.sub('一','1',ch)
	ch = re.sub('甲方','1',ch)
	ch = re.sub('二','2',ch)
	ch = re.sub('乙方','2',ch)
	ch = re.sub('三','3',ch)
	ch = re.sub('四','4',ch)
	ch = re.sub('五','5',ch)
	ch = re.sub('六','6',ch)
	ch = re.sub('七','7',ch)
	ch = re.sub('八','8',ch)
	ch = re.sub('九','9',ch)
	ch = re.sub('兩','2',ch)
	ch = re.sub('两','2',ch)

	ch_dig_dic = {}
	ch_dig_dic.setdefault('十',10)
	ch_dig_dic.setdefault('百',100)
	ch_dig_dic.setdefault('千',1000)
	ch_dig_dic.setdefault('万',10000)
	ch_dig_dic.setdefault('萬',10000)
	ch_dig_dic.setdefault('亿',100000000)
	ch_dig_dic.setdefault('億',100000000)
	ch_dig_dic.setdefault('兆',1000000000000)

	RE = '[十百千万亿萬億兆]'.decode('utf8')

	chl = ch_num_token(ch)

	#set initial value
	digit = 0
	num = 0
	lv = 0

	for c in chl:
		match = re.finditer(RE, c)
		for word in match:
			if lv < ch_dig_dic[c.encode('utf8')]:
				if num == 0 and c == '十'.decode('utf8'):
					digit = digit + ch_dig_dic[c.encode('utf8')]
					continue
				elif num == 0:
					num = num * ch_dig_dic[c.encode('utf8')]
				else:
					digit = digit + num
				num = 0
				digit = digit * ch_dig_dic[c.encode('utf8')]
			else:
				num = num * ch_dig_dic[c.encode('utf8')]
			lv = ch_dig_dic[c.encode('utf8')]
			continue
		
		try:
			float(c)
			if num != 0 and num != 10:
				digit = digit + num
				num = 0

			num = num + float(c)
		except:
			continue

	if num != 0:
		digit = digit + num
		num = 0

	if digit % 1 == 0:
		return str(int(digit))
	else:
		return str(digit)




# count the levenshtein distance-----------------------------------------------------------
##################################################
def levenshtein(first,second):  
	if len(first) > len(second):  
		first,second = second,first  
	if len(first) == 0:  
		return len(second)  
	if len(second) == 0:  
		return len(first)  
	first_length = len(first) + 1  
	second_length = len(second) + 1  
	distance_matrix = [range(second_length) for x in range(first_length)]   

	#print distance_matrix  
	for i in range(1,first_length):  
		for j in range(1,second_length):  
			deletion = distance_matrix[i-1][j] + 1  
			insertion = distance_matrix[i][j-1] + 1  
			substitution = distance_matrix[i-1][j-1]  
			if first[i-1] != second[j-1]:  
				substitution += 1  
			distance_matrix[i][j] = min(insertion,deletion,substitution)  

	#print distance_matrix  
	return distance_matrix[first_length-1][second_length-1]




# alignment the words from two corpus ***(Not finish, will make mistake)***----------------------
##################################################
def alignment(l_en, l_zh):
	al = []

	l_en_tag = []
	l_zh_tag = []
	for i in range(0, len(l_en)):
		l_en_tag.append(True)
	for i in range(0, len(l_zh)):
		l_zh_tag.append(True)
	
	# compare the word in the lists and pair them
	for distance in [0,1,2,3,4]:
		for i in range(0, len(l_en)):
			if not l_en_tag[i]:
				continue
	
			for j in range(0, len(l_zh)):
				if not l_zh_tag[j] or not l_en_tag[i]:
					continue
	
				if l_en[i][1] != l_zh[j][1]:
					continue
				
				# the No. of type number is 4 here
				if l_en[i][1] == 4 and Bi_olan == 'en' and Bi_tlan == 'zh':
					d = levenshtein(en_di(l_en[i][0]),zh_di(l_zh[j][0]))
				elif l_en[i][1] ==4 and Bi_olan == 'zh' and Bi_tlan == 'en':
					d = levenshtein(zh_di(l_en[i][0]),en_di(l_zh[j][0]))
				elif l_en[i][1] == 4 and Bi_olan == 'pt' and Bi_tlan == 'zh':
					d = levenshtein(pt_di(l_en[i][0]),zh_di(l_zh[j][0]))
				elif l_en[i][1] ==4 and Bi_olan == 'zh' and Bi_tlan == 'pt':
					d = levenshtein(zh_di(l_en[i][0]),pt_di(l_zh[j][0]))
				else:
					d = levenshtein(l_en[i][0], l_zh[j][0])
	
				if l_en[i][1] != 4 and distance == 4:
					distance = 50
				elif l_en[i][1] == 4 and distance == 50:
					distance = 4

				if d > distance:
					continue
				else:
					al.append((l_en[i][0], l_zh[j][0], l_en[i][1]))
					l_en_tag[i] = False
					l_zh_tag[j] = False
	
	for i in range(0,len(l_en_tag)):
		if l_en_tag[i]:
			al.append((l_en[i][0], 'None', l_en[i][1]))
			l_en_tag[i] = False
	
	for j in range(0,len(l_zh_tag)):
		if l_zh_tag[j]:
			al.append(('None', l_zh[j][0], l_zh[j][1]))
			l_zh_tag[j] = False

	# sort the list
	al_tag = []
	for i in range(0, len(al)):
		al_tag.append(True)

	sort_al = []
	count = 0
	for i in range(0, len(l_en)):
		for j in range(0, len(al)):
			if not al_tag[j]:
				continue
			if al[j][0] is l_en[i][0] and al[j][2] is l_en[i][1]:
				sort_al.append(al[j])
				al_tag[j] = False

	for i in range(0, len(al)):
		if al_tag[i]:
			sort_al.append(al[i])

	return sort_al

dicfile = open("/home/luyi/zh-pt-worker-v1/worker/generalization/worddic","r").readlines()
worddic={}
for line in dicfile:
	source,target=line.decode('utf8').lstrip().rstrip().split('\t')
	#print source,target
	worddic[source.lstrip().rstrip()]=target.lstrip().rstrip()
#print worddic
def Max_match_zh(line):
    chars = line  
    words = []  
    idx = 0  
    while idx < len(chars):  
        matched = False  
        for i in xrange(len(chars), 0, -1):  	
            cand=chars[idx:idx+i]#.encode("utf8")  
            #print cand,idx,i
            if cand in worddic:  
                words.append((cand.encode('utf8'),worddic[cand].encode('utf8')))		
                line=line.replace(cand, 'dwordsb', 1)
                #print cand,worddic[cand]		
                matched = True  
                break  
        if not matched:   
            i = 1  
            #words.append(chars[idx].encode("utf8"))  
        idx += i
    #print words
    return line, words
	
def sentenceMain(infilename,pTypel, singleLanguage):
	
	import jieba
	language_type = get_LanguageType()
	Symbol = get_Symbol()
	lineNum = 0
	
	# check the language type
	if singleLanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()

	sLanguage = singleLanguage

	
	outf = ""
	lexf = ""
	
	# get the RE from RE_Base.py
	sRE = get_RE(sLanguage, pTypel, False)
	
	# launch to scan and replace the corpus

		
		# the word match with the RE will be save in tuple (word, type)
		# the tuple will be save to a list for the words in one line
	lexlist = []
	words_list = []
	sentences = []
	for line in infilename:	
		conform = False
		pline, words = Max_match_zh(line)
		# do the match
		for spre in sRE:
			recomp = re.compile(sRE[spre].decode('utf8'))
		#print sRE[spre],pline
			smatch = recomp.finditer(pline)
				
			for word in smatch:
				conform = True
				lexlist.append((word.group().encode('utf8'), spre))
				pline = re.sub(word.group(), Symbol[spre], pline, count = 1)
		sentences.append(' '.join( jieba.cut(pline)))
		words_list += words
		#sentences.append(pline)
	return sentences,lexlist,words_list
		# print the result to the files basic on the user option
	#lexf.write(str(lineNum) + ' ||| ' + lex[0] + ' ||| ' + Symbol[lex[1]] + '\n')

		

##################################################
def SinMain(infilename, outfilename, otfilename, no_pattern, bilexiconFormat, option, pTypel, singleLanguage, multiprocessing, lines_deviation):
	if no_pattern:
		npa = False
		npal = []
		npalc = no_pattern.split('/')
	
		for i in npalc:
			if i != 'n':
				try:
					num = int(i)
				except:
					print '**Option -p \'s parameter must be integer.'
					call(['python',Patter_path, '-h'])
					quit()
				
				if num <= 0:
					print '**Option -p \'s parameter must be integer bigger than 0.'
					call(['python',Patter_path, '-h'])
					quit()
				
				npal.append(num)
			else:
				npa = True
				break
	
	language_type = get_LanguageType()
	Symbol = get_Symbol()
	if multiprocessing:
		lineNum = lines_deviation * (int(multiprocessing) - 1) + int(multiprocessing) - 1
	else:
		lineNum = 0
	
	# check the language type
	if singleLanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()

	sLanguage = singleLanguage

	# open the input file
	if multiprocessing:
		try:
			inf = open(infilename + '.' + sLanguage + '.' + multiprocessing , 'r')
		except:
			print '**File \'%s.' % infilename + sLanguage + '.' + multiprocessing + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	else:
		try:
			inf = open(infilename + '.' + sLanguage, 'r')
		except:
			print '**File \'%s.' % infilename + sLanguage + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	
	# open the output file and lexfile to save the words are replaced
	if multiprocessing:
		outf = open(outfilename + '.pat.' + sLanguage + '.' + multiprocessing, 'w')
		lexf = open(otfilename + '.lex.' + sLanguage + '.' + multiprocessing, 'w')
	else:
		outf = open(outfilename + '.pat.' + sLanguage, 'w')
		lexf = open(otfilename + '.lex.' + sLanguage, 'w')
	
	# open the p file and u file if the user want
	if no_pattern:
		if multiprocessing:
			pf = open(outfilename + '.p.' + sLanguage + '.' + multiprocessing, 'w')
			uf = open(outfilename + '.u.' + sLanguage + '.' + multiprocessing, 'w')
		else:
			pf = open(outfilename + '.p.' + sLanguage, 'w')
			uf = open(outfilename + '.u.' + sLanguage, 'w')
	
	# get the RE from RE_Base.py
	sRE = get_RE(sLanguage, pTypel, False)
	
	# launch to scan and replace the corpus
	while True:
		line = inf.readline().decode('utf8')
		
		no_singlelpattern = 0
		
		# print the finish message if no more lines
		if not line:
			'''
			print '\n########Completed.########'
			'''
			if multiprocessing:
				print '\nFinish part ' + multiprocessing + '.'
				break
			else:
				sys.stdout.write('\nFinish.(at line %d)\n' % lineNum)
				break
		
		lineNum = lineNum + 1
		
		# the word match with the RE will be save in tuple (word, type)
		# the tuple will be save to a list for the words in one line
		lexlist = []
		pline = line
		
		conform = False
		
		# do the match
		for spre in sRE:
			recomp = re.compile(sRE[spre].decode('utf8'))
			smatch = recomp.finditer(pline)
				
			for word in smatch:
				conform = True
				lexlist.append((word.group().encode('utf8'), spre))
				pline = re.sub(word.group(), Symbol[spre], pline, count = 1)
				no_singlelpattern = no_singlelpattern + 1
		
		# print the result to the files basic on the user option
		if (no_pattern == None and conform) or (no_pattern != None and no_singlelpattern in npal and npa == False) or (no_pattern != None and npa == True and conform):
			outf.write(pline.encode('utf8'))
			if bilexiconFormat:
				for lex in lexlist:
					lexf.write(str(lineNum) + ' ||| ' + lex[0] + ' ||| ' + Symbol[lex[1]] + '\n')
			else:
				lexf.write(str(lineNum) + ' ||| ')
				for lex in lexlist:
					lexf.write(lex[0] + ' ')
				lexf.write('\n')
			
			if option is '0':
				lexf.write(pline.encode('utf8'))
				lexf.write('\n')
			elif option is '1':
				lexf.write(line.encode('utf8'))
				lexf.write('\n')
			elif option is '2':
				lexf.write(pline.encode('utf8'))
				lexf.write(line.encode('utf8'))
				lexf.write('\n')
		else:
			outf.write(line.encode('utf8'))
		
		if no_pattern:
			if npa:
				if conform:
					pf.write(line.encode('utf8'))
				else:
					uf.write(line.encode('utf8'))
			else:
				if no_singlelpattern in npal:
					pf.write(line.encode('utf8'))
				else:
					uf.write(line.encode('utf8'))
		
		# print out which line is scanning
		if multiprocessing:
			if (lineNum % 5000 is 0):
				sys.stdout.write('.')
		else:
			if (lineNum % 1000 is 0):
				if (lineNum % 5000 is 0):
					sys.stdout.write('%d\n' % lineNum)
				else:
					sys.stdout.write('.')
		
		'''
		sys.stdout.write('\r%d lines finished.' % lineNum)
		sys.stdout.flush()
		'''
	
	# after finish, close the files and quit the program
	inf.close()
	outf.close()
	lexf.close()
	if no_pattern:
		pf.close()
		uf.close()

		
		

##################################################
def SinDicMain(infilename, outfilename, otfilename, no_pattern, bilexiconFormat, option, pTypel, singleLanguage, multiprocessing, lines_deviation):
	if no_pattern:
		npa = False
		npal = []
		npalc = no_pattern.split('/')
	
		for i in npalc:
			if i != 'n':
				try:
					num = int(i)
				except:
					print '**Option -p \'s parameter must be integer.'
					call(['python',Patter_path, '-h'])
					quit()
				
				if num <= 0:
					print '**Option -p \'s parameter must be integer bigger than 0.'
					call(['python',Patter_path, '-h'])
					quit()
				
				npal.append(num)
			else:
				npa = True
				break
				
	language_type = get_LanguageType()
	Symbol = get_Symbol()
	if multiprocessing:
		lineNum = lines_deviation * (int(multiprocessing) - 1) + int(multiprocessing) - 1
	else:
		lineNum = 0
	
	# check the language type
	if singleLanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()

	sLanguage = singleLanguage
	
	# open the input file
	if multiprocessing:
		try:
			inf = open(infilename + '.' + sLanguage + '.' + multiprocessing, 'r')
		except:
			print '**File \'%s.' % infilename + sLanguage + '.' + multiprocessing + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	else:
		try:
			inf = open(infilename + '.' + sLanguage, 'r')
		except:
			print '**File \'%s.' % infilename + sLanguage + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	# open the output file and lexfile to save the words are replaced
	if multiprocessing:
		outf = open(outfilename + '.pat.' + sLanguage + '.' + multiprocessing, 'w')
		lexf = open(otfilename + '.lex.' + sLanguage + '.' + multiprocessing, 'w')
	else:
		outf = open(outfilename + '.pat.' + sLanguage, 'w')
		lexf = open(otfilename + '.lex.' + sLanguage, 'w')
	
	# open the p file and u file if the user want
	if no_pattern:
		if multiprocessing:
			pf = open(outfilename + '.p.' + sLanguage + '.' + multiprocessing, 'w')
			uf = open(outfilename + '.u.' + sLanguage + '.' + multiprocessing, 'w')
		else:
			pf = open(outfilename + '.p.' + sLanguage, 'w')
			uf = open(outfilename + '.u.' + sLanguage, 'w')
		
	# get the RE from RE_Base.py
	sRE = get_RE(sLanguage, pTypel, True)
	
	# launch to scan and replace the corpus
	while True:
		line = inf.readline().decode('utf8')
		
		no_singlelpattern = 0
		
		# print the finish message if no more lines
		if not line:
			'''
			print '\n########Completed.########'
			'''
			if multiprocessing:
				print '\nFinish part ' + multiprocessing + '.'
				break
			else:
				sys.stdout.write('\nFinish.(at line %d)\n' % lineNum)
				break
		
		lineNum = lineNum + 1
		
		# the word match with the RE will be save in tuple (word, type)
		# the tuple will be save to a list for the words in one line
		lexlist = []
		pline = line
		
		conform = False
		
		# do the match
		for spre in sRE:
			recomp = re.compile(sRE[spre].decode('utf8'))
			smatch = recomp.finditer(pline)
			deviation = 0				
				
			for word in smatch:
				check_dic  = True
				word_start = word.start() + deviation
				
				for word_l in range(1,5):
					head = word_start - word_l + 1
					while head < 0:
						head += 1
					while True:
						if head > word_start or head + word_l > len(pline) - 1:
							break
						if find_word(pline[head:head+word_l].encode('utf8')):
							check_dic = False
							break
						head += 1
					if check_dic == False:
						break
				
				if check_dic:
					conform = True
					lexlist.append((word.group().encode('utf8'), spre))
					pline = re.sub(word.group(), Symbol[spre], pline, count = 1)
					deviation += (-word.end()+word.start()+len(Symbol[spre]))
					no_singlelpattern = no_singlelpattern + 1
		
		# print the result to the files basic on the user option
		if (no_pattern == None and conform) or (no_pattern != None and no_singlelpattern in npal and npa == False) or (no_pattern != None and npa == True and conform):
			outf.write(pline.encode('utf8'))
			if bilexiconFormat:
				for lex in lexlist:
					lexf.write(str(lineNum) + ' ||| ' + lex[0] + ' ||| ' + Symbol[lex[1]] + '\n')
			else:
				lexf.write(str(lineNum) + ' ||| ')
				for lex in lexlist:
					lexf.write(lex[0] + ' ')
				lexf.write('\n')
			
			if option is '0':
				lexf.write(pline.encode('utf8'))
				lexf.write('\n')
			elif option is '1':
				lexf.write(line.encode('utf8'))
				lexf.write('\n')
			elif option is '2':
				lexf.write(pline.encode('utf8'))
				lexf.write(line.encode('utf8'))
				lexf.write('\n')
		else:
			outf.write(line.encode('utf8'))
		
		if no_pattern:
			if npa:
				if conform:
					pf.write(line.encode('utf8'))
				else:
					uf.write(line.encode('utf8'))
			else:
				if no_singlelpattern in npal:
					pf.write(line.encode('utf8'))
				else:
					uf.write(line.encode('utf8'))
		
		# print out which line is scanning
		if multiprocessing:
			if (lineNum % 5000 is 0):
				sys.stdout.write('.')
		else:
			if (lineNum % 1000 is 0):
				if (lineNum % 5000 is 0):
					sys.stdout.write('%d\n' % lineNum)
				else:
					sys.stdout.write('.')
		
		'''
		sys.stdout.write('\r%d lines finished.' % lineNum)
		sys.stdout.flush()
		'''
	
	# after finish, close the files and quit the program
	inf.close()
	outf.close()
	lexf.close()
	if no_pattern:
		pf.close()
		uf.close()

		
		

##################################################
def BiMain(infilename, outfilename, otfilename, no_pattern, bilexiconFormat, option, pTypel, olanguage, tlanguage, nonone, multiprocessing, lines_deviation):
	global Bi_olan
	global Bi_tlan
	Bi_olan = olanguage
	Bi_tlan = tlanguage

	if no_pattern:
		npa = False
		npal = []
		npalc = no_pattern.split('/')
	
		for i in npalc:
			if i != 'n':
				try:
					num = int(i)
				except:
					print '**Option -p \'s parameter must be integer.'
					call(['python',Patter_path, '-h'])
					quit()
				
				if num <= 0:
					print '**Option -p \'s parameter must be integer bigger than 0.'
					call(['python',Patter_path, '-h'])
					quit()
				
				npal.append(num)
			else:
				npa = True
				break
				
	language_type = get_LanguageType()
	Symbol = get_Symbol()
	if multiprocessing:
		lineNum = lines_deviation * (int(multiprocessing) - 1) + int(multiprocessing) - 1
	else:
		lineNum = 0
	
	if olanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()
	
	if tlanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()
		
	oRE = get_RE(olanguage, pTypel,False)
	tRE = get_RE(tlanguage, pTypel,False)
	
	# open the input file
	if multiprocessing:
		try:
			oinf = open(infilename + '.' + olanguage + '.' + multiprocessing, 'r')
			tinf = open(infilename + '.' + tlanguage + '.' + multiprocessing, 'r')
		except:
			print '**File \'%s.en' % infilename + '.' + multiprocessing + '\' or \'%s.zh' % infilename + '.' + multiprocessing + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	else:
		try:
			oinf = open(infilename + '.' + olanguage, 'r')
			tinf = open(infilename + '.' + tlanguage, 'r')
		except:
			print '**File \'%s.en\' or \'%s.zh\' is not exist.' % (infilename, infilename)
			call(['python',Patter_path,'-h'])
			quit()
	
	# open the output file and bilexicon file
	if multiprocessing:
		ooutf = open(outfilename + '.pat.' + olanguage + '.' + multiprocessing, 'w')
		toutf = open(outfilename + '.pat.' + tlanguage + '.' + multiprocessing, 'w')
		otf = open(otfilename + '.' + olanguage + '-' + tlanguage + '.' + multiprocessing, 'w')
	else:
		ooutf = open(outfilename + '.pat.' + olanguage, 'w')
		toutf = open(outfilename + '.pat.' + tlanguage, 'w')
		otf = open(otfilename + '.' + olanguage + '-' + tlanguage, 'w')
	
	# open the p file and u file by the user option
	if no_pattern:
		if multiprocessing:
			opf = open(outfilename + '.p.' + olanguage + '.' + multiprocessing, 'w')
			ouf = open(outfilename + '.u.' + olanguage + '.' + multiprocessing, 'w')
			tpf = open(outfilename + '.p.' + tlanguage + '.' + multiprocessing, 'w')
			tuf = open(outfilename + '.u.' + tlanguage + '.' + multiprocessing, 'w')
		else:
			opf = open(outfilename + '.p.' + olanguage, 'w')
			ouf = open(outfilename + '.u.' + olanguage, 'w')
			tpf = open(outfilename + '.p.' + tlanguage, 'w')
			tuf = open(outfilename + '.u.' + tlanguage, 'w')
	
	# launch to scan and replace
	while True:
		oline = oinf.readline().decode('utf8')
		tline = tinf.readline().decode('utf8')
		
		no_opattern = 0
		no_tpattern = 0
		
		if not oline or not tline:
			'''
			if not oline and not tline:
				print '\n########Completed.########'
			else:
				print '\n########Number of lines is NOT balanced.########'
			'''
			if multiprocessing:
				print '\nFinish part ' + multiprocessing + '.'
				break
			else:
				sys.stdout.write('\nFinish.(at line %d)\n' % lineNum)
				break
		
		lineNum = lineNum + 1
		
		oconform = False
		tconform = False
		
		# the word match with the RE will be save in tuple (word, type)
		# the tuple will be save in a list, one list means one line
		finalList = []
		opline = oline
		tpline = tline
		
		# do the match
		for pre in oRE:
			olist = []
			tlist = []
			orecomp = re.compile(oRE[pre].decode('utf8'))
			trecomp = re.compile(tRE[pre].decode('utf8'))
			omatch = orecomp.finditer(opline)
			tmatch = trecomp.finditer(tpline)
			
			for word in omatch:
				olist.append((word.group().encode('utf8'), pre))
			
			for word in tmatch:
				tlist.append((word.group().encode('utf8'), pre))
	
			aliglist = alignment(olist, tlist)
			
			delnoneli = []
			if nonone:
				for i in range(0,len(aliglist)):
					if aliglist[i][0] == 'None' or aliglist[i][1] == 'None':
						delnoneli.append(i)

				count = 0 
				for i in delnoneli:
					if aliglist[i-count][1] == 'None':
						for j in range(0, len(olist)):
							if aliglist[i-count][0] == olist[j][0] and aliglist[i-count][2] == olist[j][1]:
								olist.pop(j)
								break
					else:
						for j in range(0, len(tlist)):
							if aliglist[i-count][1] == tlist[j][0] and aliglist[i-count][2] == tlist[j][1]:
								tlist.pop(j)
								break
					
					aliglist.pop(i-count)
					count+=1
				
				for i in olist:
					oconform = True
					opline = re.sub(i[0].decode('utf8'), Symbol[i[1]], opline, count = 1)
					no_opattern = no_opattern + 1
				for i in tlist:
					tconform = True
					tpline = re.sub(i[0].decode('utf8'), Symbol[i[1]], tpline, count = 1)
					no_tpattern = no_tpattern + 1
			else:
				for i in olist:
						oconform = True
						opline = re.sub(i[0].decode('utf8'), Symbol[i[1]], opline, count = 1)
						no_opattern = no_opattern + 1
				for i in tlist:
						tconform = True
						tpline = re.sub(i[0].decode('utf8'), Symbol[i[1]], tpline, count = 1)
						no_tpattern = no_tpattern + 1
						
			finalList = finalList + aliglist
		
		# print the result to the files basic on the user option
		if (no_pattern == None and (oconform or tconform)) or (no_pattern != None and no_opattern == no_tpattern and len(finalList) in npal and npa == False) or (no_pattern != None and npa == True and (oconform or tconform) and (no_opattern == no_tpattern)):
			ooutf.write(opline.encode('utf8'))
			toutf.write(tpline.encode('utf8'))
			
			if bilexiconFormat:
				for i in finalList:
					otf.write(str(lineNum) + ' ||| ' + str(i[0]) + ' ||| ' + str(i[1]) + ' ||| ' + Symbol[i[2]] + '\n')
			else:
				otf.write(str(lineNum) + ' ||| ' + str(len(finalList)) + ' ||| ')
				for i in finalList:
					otf.write(i[0] + ' ')
				otf.write('||| ')
				for i in finalList:
					otf.write(i[1] + ' ')
				otf.write('\n')
			
			if option:
				if option is '0':
					otf.write(opline.encode('utf8'))
					otf.write(tpline.encode('utf8'))
					otf.write('\n')
				elif option is '1':
					otf.write(oline.encode('utf8'))
					otf.write(tline.encode('utf8'))
					otf.write('\n')
				elif option is '2':
					otf.write(opline.encode('utf8'))
					otf.write(tpline.encode('utf8'))
					otf.write(oline.encode('utf8'))
					otf.write(tline.encode('utf8'))
					otf.write('\n')
		else:
			ooutf.write(oline.encode('utf8'))
			toutf.write(tline.encode('utf8'))
		
		if no_pattern:
			if npa:
				if oconform or tconform:
					opf.write(oline.encode('utf8'))
					tpf.write(tline.encode('utf8'))
				else:
					ouf.write(oline.encode('utf8'))
					tuf.write(tline.encode('utf8'))
			else:
				if no_opattern == no_tpattern and no_opattern in npal:
					opf.write(oline.encode('utf8'))
					tpf.write(tline.encode('utf8'))
				else:
					ouf.write(oline.encode('utf8'))
					tuf.write(tline.encode('utf8'))
		
		# print out which line is scanning
		if multiprocessing:
			if (lineNum % 5000 is 0):
				sys.stdout.write('.')
		else:
			if (lineNum % 1000 is 0):
				if (lineNum % 5000 is 0):
					sys.stdout.write('%d\n' % lineNum)
				else:
					sys.stdout.write('.')
		
		'''
		sys.stdout.write('\r%d lines finished.' % lineNum)
		sys.stdout.flush()
		'''
	
	# after finish, close the files and quit the program
	oinf.close()
	tinf.close()
	ooutf.close()
	toutf.close()
	otf.close()
	if no_pattern:
		opf.close()
		ouf.close()
		tpf.close()
		tuf.close()

		
		

##################################################
def BiDicMain(infilename, outfilename, otfilename, no_pattern, bilexiconFormat, option, pTypel, olanguage, tlanguage, nonone, multiprocessing, lines_deviation):
	global Bi_olan
	global Bi_tlan
	Bi_olan = olanguage
	Bi_tlan = tlanguage

	if no_pattern:
		npa = False
		npal = []
		npalc = no_pattern.split('/')
	
		for i in npalc:
			if i != 'n':
				try:
					num = int(i)
				except:
					print '**Option -p \'s parameter must be integer.'
					call(['python',Patter_path, '-h'])
					quit()
				
				if num <= 0:
					print '**Option -p \'s parameter must be integer bigger than 0.'
					call(['python',Patter_path, '-h'])
					quit()
				
				npal.append(num)
			else:
				npa = True
				break
				
	language_type = get_LanguageType()
	Symbol = get_Symbol()
	if multiprocessing:
		lineNum = lines_deviation * (int(multiprocessing) - 1) + int(multiprocessing) - 1
	else:
		lineNum = 0
	
	if olanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()
	
	if tlanguage not in language_type:
		print '**The program can only process language:'
		print language_type
		call(['python',Patter_path,'-h'])
		quit()
		
	oRE = get_RE(olanguage, pTypel,True)
	tRE = get_RE(tlanguage, pTypel,True)
	
	# open the input file
	if multiprocessing:
		try:
			oinf = open(infilename + '.' + olanguage + '.' + multiprocessing, 'r')
			tinf = open(infilename + '.' + tlanguage + '.' + multiprocessing, 'r')
		except:
			print '**File \'%s.en' % infilename + '.' + multiprocessing + '\' or \'%s.zh' % infilename + '.' + multiprocessing + '\' is not exist.'
			call(['python',Patter_path,'-h'])
			quit()
	else:
		try:
			oinf = open(infilename + '.' + olanguage, 'r')
			tinf = open(infilename + '.' + tlanguage, 'r')
		except:
			print '**File \'%s.en\' or \'%s.zh\' is not exist.' % (infilename, infilename)
			call(['python',Patter_path,'-h'])
			quit()
	
	# open the output file and bilexicon file
	if multiprocessing:
		ooutf = open(outfilename + '.pat.' + olanguage + '.' + multiprocessing, 'w')
		toutf = open(outfilename + '.pat.' + tlanguage + '.' + multiprocessing, 'w')
		otf = open(otfilename + '.' + olanguage + '-' + tlanguage + '.' + multiprocessing, 'w')
	else:
		ooutf = open(outfilename + '.pat.' + olanguage, 'w')
		toutf = open(outfilename + '.pat.' + tlanguage, 'w')
		otf = open(otfilename + '.' + olanguage + '-' + tlanguage, 'w')
	
	# open the p file and u file by the user option
	if no_pattern:
		if multiprocessing:
			opf = open(outfilename + '.p.' + olanguage + '.' + multiprocessing, 'w')
			ouf = open(outfilename + '.u.' + olanguage + '.' + multiprocessing, 'w')
			tpf = open(outfilename + '.p.' + tlanguage + '.' + multiprocessing, 'w')
			tuf = open(outfilename + '.u.' + tlanguage + '.' + multiprocessing, 'w')
		else:
			opf = open(outfilename + '.p.' + olanguage, 'w')
			ouf = open(outfilename + '.u.' + olanguage, 'w')
			tpf = open(outfilename + '.p.' + tlanguage, 'w')
			tuf = open(outfilename + '.u.' + tlanguage, 'w')
	
	# launch to scan and replace
	while True:
		oline = oinf.readline().decode('utf8')
		tline = tinf.readline().decode('utf8')
		
		no_opattern = 0
		no_tpattern = 0
		
		if not oline or not tline:
			'''
			if not oline and not tline:
				print '\n########Completed.########'
			else:
				print '\n########Number of lines is NOT balanced.########'
			'''
			if multiprocessing:
				print '\nFinish part ' + multiprocessing + '.'
				break
			else:
				sys.stdout.write('\nFinish.(at line %d)\n' % lineNum)
				break
		
		lineNum = lineNum + 1
		
		oconform = False
		tconform = False
		
		# the word match with the RE will be save in tuple (word, type)
		# the tuple will be save in a list, one list means one line
		finalList = []
		opline = oline
		tpline = tline
		
		# do the match
		for pre in oRE:
			olist = []
			tlist = []
			orecomp = re.compile(oRE[pre].decode('utf8'))
			trecomp = re.compile(tRE[pre].decode('utf8'))
			omatch = orecomp.finditer(opline)
			tmatch = trecomp.finditer(tpline)
			deviation = 0
			
			for word in omatch:
				check_dic  = True
				word_start = word.start()
				
				for word_l in range(1,10):
					head = word_start - word_l + 1
					while head < 0:
						head += 1
					while True:
						if head > word_start or head + word_l > len(opline) - 1:
							break
						if find_word(opline[head:head+word_l].encode('utf8')):
							check_dic = False
							break
						head += 1
					if check_dic == False:
						break
				
				if check_dic:
					olist.append((word.group().encode('utf8'), pre))
			
			deviation = 0
			
			for word in tmatch:
				check_dic  = True
				word_start = word.start()
				
				for word_l in range(1,10):
					head = word_start - word_l + 1
					while head < 0:
						head += 1
					while True:
						if head > word_start or head + word_l > len(tpline) - 1:
							break
						if find_word(tpline[head:head+word_l].encode('utf8')):
							check_dic = False
							break
						head += 1
					if check_dic == False:
						break
				
				if check_dic:
					tlist.append((word.group().encode('utf8'), pre))
	
			aliglist = alignment(olist, tlist)
			
			delnoneli = []
			if nonone:
				for i in range(0,len(aliglist)):
					if aliglist[i][0] == 'None' or aliglist[i][1] == 'None':
						delnoneli.append(i)

				count = 0 
				for i in delnoneli:
					if aliglist[i-count][1] == 'None':
						for j in range(0, len(olist)):
							if aliglist[i-count][0] == olist[j][0] and aliglist[i-count][2] == olist[j][1]:
								olist.pop(j)
								break
					else:
						for j in range(0, len(tlist)):
							if aliglist[i-count][1] == tlist[j][0] and aliglist[i-count][2] == tlist[j][1]:
								tlist.pop(j)
								break
					
					aliglist.pop(i-count)
					count+=1
				
				for i in olist:
					oconform = True
					opline = re.sub(i[0].decode('utf8'), Symbol[i[1]], opline, count = 1)
					no_opattern = no_opattern + 1
				for i in tlist:
					tconform = True
					tpline = re.sub(i[0].decode('utf8'), Symbol[i[1]], tpline, count = 1)
					no_tpattern = no_tpattern + 1
			else:
				for i in olist:
						oconform = True
						opline = re.sub(i[0].decode('utf8'), Symbol[i[1]], opline, count = 1)
						no_opattern = no_opattern + 1
				for i in tlist:
						tconform = True
						tpline = re.sub(i[0].decode('utf8'), Symbol[i[1]], tpline, count = 1)
						no_tpattern = no_tpattern + 1
						
			finalList = finalList + aliglist
		
		# print the result to the files basic on the user option
		if (no_pattern == None and (oconform or tconform)) or (no_pattern != None and no_opattern == no_tpattern and len(finalList) in npal and npa == False) or (no_pattern != None and npa == True and (oconform or tconform) and (no_opattern == no_tpattern)):
			ooutf.write(opline.encode('utf8'))
			toutf.write(tpline.encode('utf8'))
			
			if bilexiconFormat:
				for i in finalList:
					otf.write(str(lineNum) + ' ||| ' + str(i[0]) + ' ||| ' + str(i[1]) + ' ||| ' + Symbol[i[2]] + '\n')
			else:
				otf.write(str(lineNum) + ' ||| ' + str(len(finalList)) + ' ||| ')
				for i in finalList:
					otf.write(i[0] + ' ')
				otf.write('||| ')
				for i in finalList:
					otf.write(i[1] + ' ')
				otf.write('\n')
			
			if option:
				if option is '0':
					otf.write(opline.encode('utf8'))
					otf.write(tpline.encode('utf8'))
					otf.write('\n')
				elif option is '1':
					otf.write(oline.encode('utf8'))
					otf.write(tline.encode('utf8'))
					otf.write('\n')
				elif option is '2':
					otf.write(opline.encode('utf8'))
					otf.write(tpline.encode('utf8'))
					otf.write(oline.encode('utf8'))
					otf.write(tline.encode('utf8'))
					otf.write('\n')
		else:
			ooutf.write(oline.encode('utf8'))
			toutf.write(tline.encode('utf8'))
		
		if no_pattern:
			if npa:
				if oconform or tconform:
					opf.write(oline.encode('utf8'))
					tpf.write(tline.encode('utf8'))
				else:
					ouf.write(oline.encode('utf8'))
					tuf.write(tline.encode('utf8'))
			else:
				if no_opattern == no_tpattern and no_opattern in npal:
					opf.write(oline.encode('utf8'))
					tpf.write(tline.encode('utf8'))
				else:
					ouf.write(oline.encode('utf8'))
					tuf.write(tline.encode('utf8'))
		
		# print out which line is scanning
		if multiprocessing:
			if (lineNum % 5000 is 0):
				sys.stdout.write('.')
		else:
			if (lineNum % 1000 is 0):
				if (lineNum % 5000 is 0):
					sys.stdout.write('%d\n' % lineNum)
				else:
					sys.stdout.write('.')
		
		'''
		sys.stdout.write('\r%d lines finished.' % lineNum)
		sys.stdout.flush()
		'''
	
	# after finish, close the files and quit the program
	oinf.close()
	tinf.close()
	ooutf.close()
	toutf.close()
	otf.close()
	if no_pattern:
		opf.close()
		ouf.close()
		tpf.close()
		tuf.close()

#---------------------------------------------------------

#encoding=utf-8
import sys
import re

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
	ch = re.sub('二','2',ch)
	ch = re.sub('三','3',ch)
	ch = re.sub('四','4',ch)
	ch = re.sub('五','5',ch)
	ch = re.sub('六','6',ch)
	ch = re.sub('七','7',ch)
	ch = re.sub('八','8',ch)
	ch = re.sub('九','9',ch)
	ch = re.sub('兩','2',ch)
	ch = re.sub('两','2',ch)
	ch = re.sub('壹','1',ch)
	ch = re.sub('貳','2',ch)
	ch = re.sub('贰','2',ch)
	ch = re.sub('叁','3',ch)
	ch = re.sub('肆','4',ch)
	ch = re.sub('伍','5',ch)
	ch = re.sub('陸','6',ch)
	ch = re.sub('陆','6',ch)
	ch = re.sub('柒','7',ch)
	ch = re.sub('捌','8',ch)
	ch = re.sub('玖','9',ch)
	ch = re.sub('零','0',ch)
	ch = re.sub('玖','9',ch)
	ch = re.sub('零','0',ch)

	
	ch_dig_dic = {}
	ch_dig_dic.setdefault('十',10)
	ch_dig_dic.setdefault('拾',10)
	ch_dig_dic.setdefault('百',100)
	ch_dig_dic.setdefault('佰',100)
	ch_dig_dic.setdefault('千',1000)
	ch_dig_dic.setdefault('仟',1000)
	ch_dig_dic.setdefault('万',10000)
	ch_dig_dic.setdefault('萬',10000)
	ch_dig_dic.setdefault('亿',100000000)
	ch_dig_dic.setdefault('億',100000000)
	ch_dig_dic.setdefault('兆',1000000000000)

	RE = '[十拾百 佰千仟 万亿萬億兆]'.decode('utf8')

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

def pt_di(ch):
	ch = re.sub(',00','',ch)
	ch = re.sub(', ',' ',ch)
	ch = re.sub(',','',ch)
	ch = re.sub(' e ',' ',ch)
	ch = re.sub('  ',' ',ch)	
	pt_num_dic={}
	pt_num_dic.setdefault('zero','0')
	pt_num_dic.setdefault('um','1')
	pt_num_dic.setdefault('dois','2')
	pt_num_dic.setdefault('três','3')
	pt_num_dic.setdefault('quatro','4')
	pt_num_dic.setdefault('cinco','5')
	pt_num_dic.setdefault('seis','6')
	pt_num_dic.setdefault('sete','7')
	pt_num_dic.setdefault('oito','8')
	pt_num_dic.setdefault('nove','9')
	pt_num_dic.setdefault('uma','1')
	pt_num_dic.setdefault('duas','2')
	pt_num_dic.setdefault('dez','10')
	pt_num_dic.setdefault('onze','11')
	pt_num_dic.setdefault('doze','12')
	pt_num_dic.setdefault('treze','13')
	pt_num_dic.setdefault('catorze','14')
	pt_num_dic.setdefault('quinze','15')
	pt_num_dic.setdefault('dezasseis','16')
	pt_num_dic.setdefault('sezassete','17')
	pt_num_dic.setdefault('dezoito','18')
	pt_num_dic.setdefault('dezanove','19')
	chl = ch.decode('utf8').split()
	for i in range(len(chl)-1):
		if chl[i].isdigit() and chl[i+1].isdigit():
			chl[i+1]=chl[i]+chl[i+1]
			chl[i]=None
	while (None in chl):
		chl.remove(None)
	for i in range(len(chl)):
		if chl[i].encode('utf8') in pt_num_dic:
			chl[i]=pt_num_dic[chl[i].encode('utf8')].decode('utf8')
	ch_dig_dic = {}
	ch_dig_dic.setdefault('vinte',20)
	ch_dig_dic.setdefault('trinta',30)
	ch_dig_dic.setdefault('quarenta',40)
	ch_dig_dic.setdefault('cinquenta',50)
	ch_dig_dic.setdefault('sessenta',60)
	ch_dig_dic.setdefault('setenta',70)
	ch_dig_dic.setdefault('oitenta',80)
	ch_dig_dic.setdefault('noventa',90)
	
	ch_dig_dic.setdefault('cem',100)
	ch_dig_dic.setdefault('cento',100)
	ch_dig_dic.setdefault('duzentos',200)
	ch_dig_dic.setdefault('duzentas',200)
	ch_dig_dic.setdefault('trezentos',300)
	ch_dig_dic.setdefault('trezentas',300)	
	ch_dig_dic.setdefault('quatrocentos',400)
	ch_dig_dic.setdefault('quatrocentas',400)	
	ch_dig_dic.setdefault('quinhentos',500)
	ch_dig_dic.setdefault('quinhentas',500)
	ch_dig_dic.setdefault('seiscentos',600)
	ch_dig_dic.setdefault('seiscentas',600)
	ch_dig_dic.setdefault('setecentos',700)
	ch_dig_dic.setdefault('setecentas',700)
	ch_dig_dic.setdefault('oitocentos',800)
	ch_dig_dic.setdefault('oitocentas',800)
	ch_dig_dic.setdefault('novecentos',900)
	ch_dig_dic.setdefault('novecentas',900)
	
	ch_dig_dic.setdefault('mil',1000)
	ch_dig_dic.setdefault('milhão',1000000)
	ch_dig_dic.setdefault('milhões',1000000)
	ch_dig_dic.setdefault('bilhões',1000000000)
	ch_dig_dic.setdefault('bilhão',1000000000)

	RE = '[vinte trinta quarenta cinquenta sessenta setenta oitenta noventa cem cento duzentos duzentas trezentos trezentas quatrocentos quatrocentas quinhentos quinhentas seiscentos seiscentas setecentos setecentas oitocentos oitocentas novecentos novecentas mil milhão milhões bilhões bilhão]'.decode('utf8')

	#chl = ch_num_token(ch).split()

	#set initial value
	digit = 0
	num = 0
	lv = 0

	for c in chl:
		if c in ch_dig_dic:
			if c in ['mil'.decode('utf8'),'milhão'.decode('utf8'),'milhões'.decode('utf8'),'bilhões'.decode('utf8'),'bilhão'.decode('utf8')]:
				num = num*ch_dig_dic[c.encode('utf8')]
				digit+=num
				num=0
			else:
				num = num + ch_dig_dic[c.encode('utf8')]
			#digit + ch_dig_dic[c.encode('utf8')]
		try:
			float(c)
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


############### main ##################

def num_translate(line,lang):
	output = ''
	process = True
	if lang=='pt':
		ordinal_dic = {'甲方\n':'primeiro','乙方\n':'segundo','丙方\n':'terceiro','丁方\n':'quarto','第一\n':'primeira','第二\n':'segunda','第三\n':'terceira','第四\n':'quarta','第五\n':'quinta','第六\n':'sexta','第七\n':'sétima','第八\n':'oitava','第九\n':'nona','第十\n':'décima','第二十\n':'vigésima', '第三十\n':'trigésima','第四十\n':'quadragésima','第五十\n':'quinquagésima','第六十\n':'sexagésima','第七十\n':'septuagésima','第八十\n':'octogésima','第九十\n':'nonagésima','第一百\n':'centésima'}
		recompi = re.compile('[第 甲方 乙方 丙方 丁方 平方米]'.decode('utf8'))
		match = recompi.finditer(line.decode('utf8'))
		for word in match:
			process = False
		if process:
			if '/' in line: output += line 
			else:output += zh_di(line) 
		else:
			if line in ordinal_dic:
				output += ordinal_dic[line]
			else:
				recompi = re.compile(r'第'.decode('utf8'))
				match = recompi.finditer(line.decode('utf8'))
				for word in match:
					process = True
				if process:
					line = re.sub(r'第', '', line, count = 1)
					line = re.sub(r'号', '', line, count = 1)
					if line[0].isdigit():ordinal = 'n.º ' + line
					else:
						ordinal = 'n.º ' + zh_di(line)
				else:
					ordinal = re.sub(r'第', 'n.º ', line, count = 1)
					ordinal = re.sub(r'号', '', ordinal, count = 1)
					ordinal = re.sub(r'平方米', ' metros quadrados', ordinal, count = 1)
				output += re.sub(r'\n', '', ordinal, count = 1)
				
	if lang=='zh'or lang == 'ch':				
		ordinal_dic = {'primeira':'第一\n','segunda':'第二\n','terceira':'第三\n','quarta':'第四\n','quinta':'第五\n','sexta':'第六\n','sétima':'第七\n','oitava':'第八\n','nona':'第九\n','décima':'第十\n','vigésima':'第二十\n', 'trigésima':'第三十\n','quadragésima':'第四十\n','quinquagésima':'第五十\n','sexagésima':'第六十\n','septuagésima':'第七十\n','octogésima':'第八十\n','nonagésima':'第九十\n','centésima':'第一百\n'}
		ordinal_dic1 = {'primeiro':'第一\n','segundo':'第二\n','terceiro':'第三\n','quarto':'第四\n','quinto':'第五\n','sexto':'第六\n','sétimo':'第七\n','oitavo':'第八\n','nono':'第九\n','décimo':'第十\n','vigésimo':'第二十\n', 'trigésimo':'第三十\n','quadragésimo':'第四十\n','quinquagésimo':'第五十\n','sexagésimo':'第六十\n','septuagésimo':'第七十\n','octogésimo':'第八十\n','nonagésimo':'第九十\n','centésimo':'第一百\n'}
		line=line.lstrip().rstrip().lower()
		if line in ordinal_dic:
			output += ordinal_dic[line]
			return output
		if line in ordinal_dic1:
			output += ordinal_dic1[line]
			return output
		line = re.sub(r'n.º',r'.º', line, count = 1)
		line = re.sub(r'.ª',r'.º', line, count = 1)
		recompi = re.compile('.º'.decode('utf8'))
		match = recompi.finditer(line.decode('utf8'))
	
		for word in match:
			process = False

		if process: output += pt_di(line) + '\n'
		else:
			line = re.sub(r'.º', '', line, count = 1)
			line=line.lstrip().rstrip()
			ordinal =r'第' + line
			#if line[0].isdigit():ordinal = r'第' + line
			#else:ordinal = r'第' + zh_di(line)
			ordinal = re.sub(r'\n', '', ordinal, count = 1)
			output += ordinal
		output=output.encode('utf8')
	return output
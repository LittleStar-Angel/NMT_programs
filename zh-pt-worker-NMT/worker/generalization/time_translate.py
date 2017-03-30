#encoding: utf-8

'''|||||||||||||||||  Time translation program  |||||||||||||||||'''
'''|||||||||||||||||         Version 2.0        |||||||||||||||||'''
'''|||||||||||||||||     Developed by WHT       |||||||||||||||||'''

import os
import sys
import re



def time_translate(original, lang):
	zh_num_set = {'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9','兩':'2','两':'2','零':'0'}
	en_num_set1 = {'um':'一','dois':'兩','três':'三','quatro':'四','cinco':'五','seis':'六','sete':'七','oito':'八','nove':'九','dez':'十','onze':'十一','doze':'十二','treze':'十三','catorze':'十四','quinze':'十五','dezesseis':'十六','dezessete':'十七','dezoito':'十八','dezenove':'十九','vinte':'二十'}
	en_nun_set2 = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
	en_day_set = {'segunda':'星期一','terça':'星期二','quarta':'星期三','quinta':'星期四','sexta':'星期五','sábado':'星期六','domingo':'星期日'}
	zh_day_set = {'星期一':'segunda-feira','星期二':'terça-feira','星期三':'quarta-feira','星期四':'quinta-feira','星期五':'sexta-feira','星期六':'sábado','星期日':'domingo'}
	zh_time_set = {'上午':'manhã','下午':'tarde','中午':'meio-dia','午夜':'meia-noite','凌晨':'meia-noite','早上':'manhã','晚上':'noite','傍晚':'noite','黃昏':'noite'}
	en_time_set = {'manhã':'上午','tarde':'下午','meio-dia':'中午','meia-noite':'午夜','noite':'晚上','noite':'傍晚'}
	en_type_max = 3
	zh_type_max = 4 
	type_num = 1
	hour = -1
	minute = -1
	second = -1
	ap = -1
	day = -1
	original = original.replace('\n','').decode('utf8')
	original = original.replace('\r','')
	original = original.replace('：'.decode('utf8'),':'.decode('utf8'))

	s = original

	if lang == 'pt':
		s = s.replace('钟'.decode('utf8'),'')
		s = s.replace('鐘'.decode('utf8'),'')
		s = s.replace('點'.decode('utf8'),'点'.decode('utf8'))
		s = s.replace('時'.decode('utf8'),'点'.decode('utf8'))
		if s.find('点'.decode('utf8')) != len(s)-1:
			s = s.replace('点'.decode('utf8'),'点 '.decode('utf8'))
		s = s.replace('半'.decode('utf8'),'30分'.decode('utf8'))
		if s.find('分'.decode('utf8')) != len(s)-1:
			s = s.replace('分'.decode('utf8'),'分 '.decode('utf8'))
		
		#################Time word############################
		for x in zh_time_set:
				s = s.replace(x.decode('utf8'),x.decode('utf8')+' '.decode('utf8'))

		################Day word################################
		s = s.replace('周'.decode('utf8'),'星期'.decode('utf8'))
		s = s.replace('週'.decode('utf8'),'星期'.decode('utf8'))
		for x in zh_day_set:
				s = s.replace(x.decode('utf8'),x.decode('utf8')+' '.decode('utf8'))

		temp = s.lstrip().rstrip().split(' ')
		if "u\'\'" in temp:
			temp.remove(u'')

		for x in range(0,len(temp)):
			if temp[x].find('点'.decode('utf8')) != -1 or temp[x].find('分'.decode('utf8')) != -1 or temp[x].find('秒'.decode('utf8')) != -1:
				if temp[x].find('十'.decode('utf8')) != -1:
					if temp[x].find('十'.decode('utf8'))+1 == len(temp[x])-1 and temp[x].find('十'.decode('utf8')) != 0:
						temp[x] = temp[x].replace('十'.decode('utf8'),'0'.decode('utf8'))
					elif temp[x].find('十'.decode('utf8')) == 0:
						if temp[x].find('十'.decode('utf8'))+1 == len(temp[x])-1:
							temp[x] = temp[x].replace('十'.decode('utf8'),'10'.decode('utf8'))
						else:
							temp[x] = temp[x].replace('十'.decode('utf8'),'1'.decode('utf8'))
					else:
						temp[x] = temp[x].replace('十'.decode('utf8'),'')
				for y in zh_num_set:
					temp[x] = temp[x].replace(y.decode('utf8'),zh_num_set[y].decode('utf8'))
				if temp[x].find('点'.decode('utf8')) != -1 and temp[x].find('点'.decode('utf8')) != 0 and temp[x][temp[x].find('点'.decode('utf8'))-1].isnumeric():
					temp[x] = temp[x].replace('点'.decode('utf8'),'')
					hour = x
				elif temp[x].find('分'.decode('utf8')) != -1 and temp[x].find('分'.decode('utf8')) != 0 and temp[x][temp[x].find('分'.decode('utf8'))-1].isnumeric():
					temp[x] = temp[x].replace('分'.decode('utf8'),'')
					minute = x
				elif temp[x].find('秒'.decode('utf8')) != -1 and temp[x].find('秒'.decode('utf8')) != 0 and temp[x][temp[x].find('秒'.decode('utf8'))-1].isnumeric():
					temp[x] = temp[x].replace('秒'.decode('utf8'),'')
					second = x
			elif temp[x].find('星期'.decode('utf8')) != -1:
				for y in zh_day_set:
					temp[x] = temp[x].replace(y.decode('utf8'), zh_day_set[y].decode('utf8'))
				day = x
			elif temp[x].encode('utf8') in zh_time_set:
				temp[x] = zh_time_set[temp[x].encode('utf8')]
				ap = x		

	############English to Chinese part(not finish yet)###############


	if lang == 'zh':
		s = s.lower()
		if s.find('horas'.decode('utf8')) != -1:
			if s.find(','.decode('utf8'))==-1:
				s=s.replace(' horas'.decode('utf8'),'点'.decode('utf8'))
			for y in en_num_set1:
				s = s.replace(y.decode('utf8'), en_num_set1[y].decode('utf8'))
		s = s.replace(' horas'.decode('utf8'),'')
		s = s.replace(','.decode('utf8'),': ')
		s = s.replace('  '.decode('utf8'),' ')
		if s.find('feira'.decode('utf8')) != -1:
			s = s.replace('feira'.decode('utf8'),'')
			s = s.replace('-'.decode('utf8'),'')
		for y in en_day_set:
			s = s.replace(y.decode('utf8'), en_day_set[y].decode('utf8'))
		time = s	
	
	######################Time word replacing#########################
	if lang == 'pt':
		if hour != -1 and ap != -1:
			if (int(temp[hour]) >= 0 and int(temp[hour]) <= 5) and temp[ap] == 'morning':
				temp[ap] = 'midnight'
			elif (int(temp[hour]) >= 5 and int(temp[hour]) <= 6) and temp[ap] == 'afternoon':
				temp[ap] = 'evening'
			elif (int(temp[hour]) >= 7 and int(temp[hour]) <= 11) and temp[ap] == 'afternoon':
				temp[ap] = 'night'


	##################Chinese output type processing###################
	if lang == 'pt':
		if len(temp) == 1 and (hour != -1 or minute != -1 or second != -1 or day != -1 or ap != -1):
			if hour != -1:
				if type_num == 0:
					if int(temp[hour]) > 12:
						temp[hour] -= 12
						time = temp[hour]+' horas'
						if int(temp[hour]) <= 4:
							 time = time +' da tarde'
						elif int(temp[hour]) >= 5 and int(temp[hour]) <= 11:
							time = time +' da noite'
					else:
						if input_file == '':
							mean_block = 1
							print('There have two meaning about this sentence')
							print('The possible translation of this sentence may be one of the following')
							if int(temp[hour]) >= 1 and int(temp[hour]) <= 5:
								print temp[hour]+' horas à meia-noite'
								if int(temp[hour]) != 5:
									print temp[hour]+' horas da tarde'
								else:
									print temp[hour]+' horas da noite'
							elif int(temp[hour]) >= 6 and int(temp[hour]) <= 11:
								print temp[hour]+' horas da manhã'
								if int(temp[hour]) != 6:
									print temp[hour]+' horas da noite'
								else:
									print temp[hour]+' horas da noite'
							elif int(temp[hour]) == 12:
								print temp[hour]+' horas ao meio dia'
								print temp[hour]+' horas à meia-noite'
						else:
							time = temp[hour]+' horas'

				elif type_num == 1 or type_num == 2:
					if int(temp[hour]) > 12:
						temp[hour] = int(temp[hour]) - 12
						if type_num == 1:
							time = temp[hour]+' p.m.'
						else:
							time = temp[hour]+' PM'
					else:
						if input_file == '':
							mean_block = 1
							print('There have two meaning about this sentence')
							print('The possible translation of this sentence may be one of the following')
							if type_num == 1:
								print temp[hour]+' a.m.'
								print temp[hour]+' p.m.'
							else:
								print temp[hour]+' AM'
								print temp[hour]+' PM'
						else:
							time = temp[hour]+' horas'

			elif minute != -1:
				time = temp[minute]+' minutos'
			elif second != -1:
				time = temp[second]+' segundo'
			elif day != -1:
				time = temp[day]
			elif ap != -1:
				time = temp[ap]
				


		elif len(temp) == 2 and ((hour != -1 and minute != -1) or (minute != -1 and second != -1) or (day != -1 and ap != -1) or (ap != -1 and hour != -1) or (day != -1 and hour != -1)):
			if minute != -1:
				if int(temp[minute].encode('utf8')) < 10 and len(temp[minute].encode('utf8')) == 1:
					temp[minute] = '0'.decode('utf8')+temp[minute]
			if second != -1:
				if int(temp[second].encode('utf8')) < 10 and len(temp[second].encode('utf8')) == 1:
					temp[second] = '0'.decode('utf8')+temp[second]


			if hour != -1 and minute != -1:
				if int(temp[hour]) > 12:
					temp[hour] = int(temp[hour]) - 12
					time = temp[hour]+':'+temp[minute]+' p.m.'
				else:
					time = temp[hour]+':'+temp[minute]

			elif minute != -1 and second != -1:
				time = temp[minute]+':'+temp[second]+"'"
			
			elif day != -1 and ap != -1:
				time = temp[day]+' '+temp[ap]

			elif day != -1 and hour != -1:
				if int(temp[hour]) > 12:
					temp[hour] = int(temp[hour]) - 12
					time = temp[day]+' '+temp[hour]+' p.m.'
				else:
					time = temp[day]+' '+temp[hour]+' horas'

			elif ap != -1 and hour != -1:
				if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
					time = temp[hour]+' a.m.'
				elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
					time = temp[hour]+' p.m.'
						
		elif len(temp) == 3 and ((hour != -1 and minute != -1 and second != -1) or (day != -1 and ap != -1 and hour != -1) or (ap != -1 and hour != -1 and minute != -1) or (day != -1 and hour != -1 and minute != -1)):
			if int(temp[minute].encode('utf8')) < 10 and len(temp[minute].encode('utf8')) == 1:
				temp[minute] = '0'.decode('utf8')+temp[minute]
			if int(temp[second].encode('utf8')) < 10 and len(temp[second].encode('utf8')) == 1:
				temp[second] = '0'.decode('utf8')+temp[second]
			if hour != -1 and minute != -1 and second != -1:
				if int(temp[hour]) > 12:
					temp[hour] = int(temp[hour]) - 12
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+' p.m.'
				else:
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+"'"

			elif day != -1 and ap != -1 and hour != -1:
				if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
					time = temp[hour]+' a.m.'+' de '+temp[day]
				elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
					time = temp[hour]+' p.m.'+' de '+temp[day]
			elif ap != -1 and hour != -1 and minute != -1:
				if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
					time = temp[hour]+':'+temp[minute]+' a.m.'
				elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
					time = temp[hour]+':'+temp[minute]+' p.m.'
			elif day != -1 and hour != -1 and minute != -1:
					if int(temp[hour]) > 12:
						temp[hour] = int(temp[hour]) - 12
						time = temp[hour]+':'+temp[minute]+' p.m.'+' de '+temp[day]
					else:
						time = temp[hour]+':'+temp[minute]+' de '+temp[day]

		elif len(temp) == 4 and ((day != -1 and ap != -1 and hour != -1 and minute != -1) or (ap != -1 and hour != -1 and minute != -1 and second != -1) or (day != -1 and hour != -1 and minute != -1 and second != -1)):
			if int(temp[minute].encode('utf8')) < 10 and len(temp[minute].encode('utf8')) == 1:
				temp[minute] = '0'.decode('utf8')+temp[minute]
			if int(temp[second].encode('utf8')) < 10 and len(temp[second].encode('utf8')) == 1:
				temp[second] = '0'.decode('utf8')+temp[second]

			if day != -1 and ap != -1 and hour != -1 and minute != -1:
				if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
					time = temp[hour]+':'+temp[minute]+' a.m.'+' de '+temp[day]
				elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
					time = temp[hour]+':'+temp[minute]+' p.m.'+' de '+temp[day]
						
			elif ap != -1 and hour != -1 and minute != -1 and second != -1:
				if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+' a.m.'
				elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+' p.m.'
			elif day != -1 and hour != -1 and minute != -1 and second != -1:
				if int(temp[hour]) > 12:
					temp[hour] = int(temp[hour]) - 12
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+"'"+' p.m.'+' de '+temp[day]
				else:
					time = temp[hour]+':'+temp[minute]+':'+temp[second]+"'"+' de '+temp[day]

		elif len(temp) == 5 and (day!= -1 and minute != -1 and second != -1 and ap != -1 and hour != -1):
			if int(temp[minute].encode('utf8')) < 10 and len(temp[minute].encode('utf8')) == 1:
				temp[minute] = '0'.decode('utf8')+temp[minute]
			if int(temp[second].encode('utf8')) < 10 and len(temp[second].encode('utf8')) == 1:
				temp[second] = '0'.decode('utf8')+temp[second]

			if temp[ap] == 'manhã' or temp[ap] == 'meia-noite':
				time = temp[hour]+':'+temp[minute]+':'+temp[second]+' a.m.'+' de '+temp[day]
			elif temp[ap] == 'meio dia' or temp[ap] == 'noite' or temp[ap] == 'tarde' :
				time = temp[hour]+':'+temp[minute]+':'+temp[second]+' p.m.'+' de '+temp[day]
		else:
			time = original
	return time.encode('utf8')	



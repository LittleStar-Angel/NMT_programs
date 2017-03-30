#encoding: utf-8
import os
import re
import sys

def date_translate(original,lang):

	zh_month_set = {'一月':'janeiro','二月':'fevereiro','三月':'marco','四月':'abril','五月':'maio','六月':'junho','七月':'julho','八月':'agosto','九月':'setembro','十月':'outubro','11月':'novembro','12月':'dezembro','1月':'janeiro','2月':'fevereiro','3月':'marco','4月':'abril','5月':'maio','6月':'junho','7月':'julho','8月':'agosto','9月':'setembro','10月':'outubro','01月':'janeiro','02月':'February','03月':'marco','04月':'abril','05月':'maio','06月':'junho','07月':'julho','08月':'agosto','09月':'setembro'}
	zh_month_set2 ={ '十一月':'novembro','十二月':'dezembro'}
	zh_year_set = {'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9','零':'0'}
	zh_day_set = {'一':'1','二':'2','三':'3','四':'4','五':'5','六':'6','七':'7','八':'8','九':'9'}

	en_month_set = {'janeiro':'一月','fevereiro':'二月','março':'三月','abril':'四月','maio':'五月','junho':'六月','julho':'七月','agosto':'八月','setembro':'九月','outubro':'十月','novembro':'十一月','dezembro':'十二月'}
	en_year_set = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九','0':'零'}
	en_day_set = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}

	en_day_word = {'primeira':'一','segunda':'二','terceira':'三','quarta':'四','quinta':'五','sexta':'六','sétima':'七','oitava':'八','nona':'九','décima':'十','décima primeira':'十一','décima segunda':'十二','décima terceira':'十三','décima quarta':'十四','décima quinta':'十五','décima sexta':'十六','décima sétima':'十七','décima oitava':'十八','décima nona':'十九','vigésima':'二十','vigésima primeira':'二十一','vigésima segunda':'二十二','vigésima terceira':'二十三','vigésima quarta':'二十四','vigésima quinta':'二十五','vigésima sexta':'二十六','vigésima sétima':'二十七','vigésima oitava':'二十八','vigésima nona':'二十九','trigésima':'三十','trigésima primeira':'三十一'}

	day = -1
	month = -1
	year = -1
	date = ''
	s = original.decode('utf8')
	if(lang == 'pt'):
		s = s.replace(' ','')
		s = s.replace('的'.decode('utf8'),'')
		s = s.replace('號'.decode('utf8'),'日 '.decode('utf8'))
		s = s.replace('号'.decode('utf8'),'日 '.decode('utf8'))
		s = s.replace('年'.decode('utf8'),'年 '.decode('utf8'))
		s = s.replace('日'.decode('utf8'),'日 '.decode('utf8'))
		s = s.replace('月'.decode('utf8'),'月 '.decode('utf8'))
		s = s.replace('  '.decode('utf8'),' ')
		temp = s.lstrip().rstrip().split(" ")
		for x in range(0,len(temp)):
			if temp[x].find('年'.decode('utf8')) != -1:
				year = x
				temp[x] = temp[x].replace('年'.decode('utf8'),'')
				for y in zh_year_set: temp[x] = temp[x].replace(y.decode('utf8'),zh_year_set[y].decode('utf8'))
			elif temp[x].find('月'.decode('utf8'))!=-1:
				month = x
				if temp[x].find('十一'.decode('utf8')) != -1 or temp[x].find('十二'.decode('utf8')) != -1:
					for y in zh_month_set2: temp[x] = temp[x].replace(y.decode('utf8'),zh_month_set2[y].decode('utf8'))
				else:
					for y in zh_month_set: temp[x] = temp[x].replace(y.decode('utf8'),zh_month_set[y].decode('utf8'))
			elif temp[x].find('日'.decode('utf8')) != -1:
				day = x
				temp[x] = temp[x].replace('日'.decode('utf8'),'')
				if temp[x].find('十'.decode('utf8')) != -1:
					pos=temp[x].find('十'.decode('utf8'))
					leng=len(temp[x])
					if pos == 0:
						if leng==1: temp[x] = temp[x].replace('十'.decode('utf8'),'10'.decode('utf8'))
						else: temp[x] = temp[x].replace('十'.decode('utf8'),'1'.decode('utf8'))
					else:
						if leng-1==pos: temp[x] = temp[x].replace('十'.decode('utf8'),'0'.decode('utf8'))
						else: temp[x] = temp[x].replace('十'.decode('utf8'),''.decode('utf8'))
				for y in zh_day_set: temp[x] = temp[x].replace(y.decode('utf8'),zh_day_set[y].decode('utf8'))
		datelist = ['','de ','','de ','']
		if day != -1 :datelist[0] = temp[day]+' '
		else:datelist[1]=''
		if month !=-1 :datelist[2] = temp[month]+' '
		else:datelist[3]=""
		if year!=-1:datelist[4]=temp[year]
		else:datelist[3]=""
		date=datelist[0]+datelist[1]+datelist[2]+datelist[3]+datelist[4]
		if month == -1 and day == -1 and year == -1:date = original

	elif (lang == 'zh' or lang == 'ch'):
		s = s.replace(', '.decode('utf8'),'')
		s = s.replace('dia '.decode('utf8'),'')
		s = s.replace('de '.decode('utf8'),'')
		s = s.replace('  '.decode('utf8'),' ')
		temp = s.lstrip().rstrip().split(" ")
		for x in range(0,len(temp)):
			if temp[x].isdigit() and (len(temp[x]) == 4):
				year = x
				for y in en_year_set:
					temp[x] = temp[x].replace(y.decode('utf8'),en_year_set[y].decode('utf8'))
			elif ((len(temp[x]) <= 2) and temp[x].isdigit()) or (temp[x].isalpha and (temp[x].lower() in en_day_word)):
				day = x				
				if temp[x].isalpha() and (temp[x].lower() in en_day_word):
					temp[x] = temp[x].lower()
					temp[x] = en_day_word[temp[x].encode('utf8')].decode('utf8')
				else:
					if(len(temp[x]) == 2) and temp[x][0] != '0'.decode('utf8'):
						if(temp[x][0] != '1'.decode('utf8')) and temp[x][1]!='0': temp[x] = temp[x][0] + '十'.decode('utf8')+temp[x][1]
						elif (temp[x][0] != '1'.decode('utf8')) and temp[x][1]=='0': temp[x] = temp[x][0] + '十'.decode('utf8')
						elif (temp[x][0] == '1'.decode('utf8')) and temp[x][1]=='0': temp[x]= '十'.decode('utf8')
						elif (temp[x][0] == '1'.decode('utf8')) and temp[x][1]!='0': temp[x]= '十'.decode('utf8') +  temp[x][1]
					for y in en_day_set: temp[x] = temp[x].replace(y.decode('utf8'),en_day_set[y].decode('utf8'))
			elif temp[x].isalpha() and (temp[x].lower() in en_month_set):
				for y in en_month_set:
					temp[x] = temp[x].lower()
					temp[x] = temp[x].replace(y.decode('utf8'),en_month_set[y].decode('utf8'))
				month = x
		datelist = ['','年'.decode('utf8'),'','','日'.decode('utf8')]
		if year!=-1:datelist[0]=temp[year]
		else:datelist[1]=""
		if month !=-1 :datelist[2] = temp[month]
		if day != -1 :datelist[3] = temp[day]
		else:datelist[4]=''
		date=datelist[0]+datelist[1]+datelist[2]+datelist[3]+datelist[4]
		if month == -1 and day == -1 and year == -1:date = original
		date=date.encode('utf8')
	return date
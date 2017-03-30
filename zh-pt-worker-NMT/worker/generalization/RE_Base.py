#encoding=utf-8


# To Add a new language:
#	1. Add a new function simulate to the "enRE", "enRE_d", "zhRE" and "zhRE_d" ("_d" means the RE use in dictionary mode),
#	   and type the RE form like them for each pattern type.
#	   If do not have the RE in some types, can use this RE '($^)' to match nothing.
#	2. Add a new item in the dictionary "functionName" and "dicfunctionName" which in "get_RE" function.
# 	3. Add a new item in the list "language_type" which locate down there.
#	
# To Add a new pattern type:
#	1. Add a new RE into each type of language's RE function
#	   by using xxREdict.setdefault(Type_num,RE).
#	2. Add a new item into the dictionary "Symbol" which locate down there.
#	3. Add a new item into the dictionary "Type_num" which locate down there.


# Declaration the global list and dictionary
Type_num = {'date':0, 'time':1, 'email':2, 'hyperlink':3, 'number':4,'words':5}

language_type = ['en','zh','pt']

Symbol = {0:'ddateb',1:'dtimeb', 2:'demailb', 3:'dhyperlinkb', 4:'dnumb',5:'dwordsb'}


# Function to get language type
def get_LanguageType():
	return language_type


# Function to get the pattern type
def get_PatternType():
	return Type_num


# Function to get the Symbol list
def get_Symbol():
	return Symbol


# Function to get the RE
def get_RE(language, reType = None, Dic = False):	
	if language not in language_type:
		return None
	
	functionName = {'en':enRE, 'zh':zhRE, 'pt':ptRE}

	dicfunctionName = {'en':enRE_d, 'zh':zhRE_d, 'pt':ptRE_d}
	
	if Dic:
		return dicfunctionName[language](reType)
	else:
		return functionName[language](reType)


# English RE_with_Trie_Tree
def enRE_d(reType):
	enRE = str()
	
	enREdict = {}
	enREdict.setdefault(0,r'([0-2]?\d|3[01])(-|\/|\.)([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)(\d{2}|\d{4})|([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)([0-2]?\d|3[01])(-|\/|\.)(\d{2}|\d{4})|([0-2]?\d|3[01]|first|third|second|[\w]+th)(th|st|rd|nd)?(\sof)?(\s(January|February|March|April|May|June|July|August|September|October|November|December))((\,)?(\s?in)?(\s(\d{4}|\s\'\d{2})))?|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|second|third|\w+th))(th|st|rd|nd)?\,?(\s?(in|of))?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sof|\,)?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|third|second|\w+th))(th|st|rd|nd)?|([12][019]\d\ds?)|\b(January|February|March|April|May|June|July|August|September|October|November|December)\b|\b\'\d{2}s\b')
	enREdict.setdefault(1,r'([0-2]?\d:[0-5][0-9](\s?[AaPp]\.?[mM]\.?\b)?|([0]?[1-9]|[1][012]|\bone\b|\btwo\b|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\so\'clock)|([0]?[1-9]|[1][1-9]|[2][0-4])\s[AaPp]\.?[Mm]\.?\b|([mM]on|[tT]ues|[wW]ednes|[tT]hurs|[fF]ri|[sS]atur|[sS]un)day')
	enREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	enREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	enREdict.setdefault(4,r'(((\d+([\,\./]\d+)*|\d+)([\s\-]([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))*|\b(([oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en|[tT]wenty|[tT]hirty|[fF]orty|[fF]ifty|[sS]ixty|[sS]eventy|[eE]ighty|[nN]inety)\b(\s([pP]oint|[oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en)\b)*)([\W]([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))*)+|\b[aA](\s([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))+)|\b[fF]irst\b|\b[sS]econd\b|\b[tT]hird\b|\b[fF]ourth\b|\b[fF]ifth\b|\b[sS]ixth\b|\b[sS]eventh\b|\b[eE]ighth\b|\b[nN]inth\b')

	if reType is None:
		return enREdict
	else:
		senREdict = {}
		for t in reType:
			senREdict.setdefault(Type_num[t], enREdict[Type_num[t]])
		return senREdict


# English RE_without_Trie_Tree
def enRE(reType):
	enRE = str()
	
	enREdict = {}
	enREdict.setdefault(0,r'([0-2]?\d|3[01])(-|\/|\.)([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)(\d{2}|\d{4})|([01]?\d|[jJ]an|[fF]eb|[mM]ar|[aA]pr|[mM]ay|[jJ]un|[jJ]ul|[aA]ug|[sS]ep|[oO]ct|[nN]ov|[dD]ec)(-|\/|\.)([0-2]?\d|3[01])(-|\/|\.)(\d{2}|\d{4})|([0-2]?\d|3[01]|first|third|second|[\w]+th)(th|st|rd|nd)?(\sof)?(\s(January|February|March|April|May|June|July|August|September|October|November|December))((\,)?(\s?in)?(\s(\d{4}|\s\'\d{2})))?|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|second|third|\w+th))(th|st|rd|nd)?\,?(\s?(in|of))?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sof|\,)?(\s\d{4}|\s\'\d{2})|(January|February|March|April|May|June|July|August|September|October|November|December)(\sthe)?(\s([012]?\d|3[01]|first|third|second|\w+th))(th|st|rd|nd)?|([12][019]\d\ds?)|\b(January|February|March|April|May|June|July|August|September|October|November|December)\b|\b\'\d{2}s\b')
	enREdict.setdefault(1,r'([0-2]?\d:[0-5][0-9](\s?[AaPp]\.?[mM]\.?\b)?|([0]?[1-9]|[1][012]|\bone\b|\btwo\b|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\so\'clock)|([0]?[1-9]|[1][012]|[2][0-4])\s[AaPp]\.?[Mm]\.?\b|([mM]on|[tT]ues|[wW]ednes|[tT]hurs|[fF]ri|[sS]atur|[sS]un)day')
	enREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	enREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	enREdict.setdefault(4,r'(((\d+([\,\./]\d+)*|\d+)([\s\-]([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))*|\b(([oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en|[tT]wenty|[tT]hirty|[fF]orty|[fF]ifty|[sS]ixty|[sS]eventy|[eE]ighty|[nN]inety)\b(\s([pP]oint|[oO]ne|[tT]wo|[tT]hree|[fF]our|[fF]ive|[sS]ix|[sS]even|[eE]ight|[nN]ine|[tT]en)\b)*)([\W]([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))*)+|\b[aA](\s([hH]undred|[mM]illion|[tT]housand|[bB]illion|[tT]rillion))+)|\b[fF]irst\b|\b[sS]econd\b|\b[tT]hird\b|\b[fF]ourth\b|\b[fF]ifth\b|\b[sS]ixth\b|\b[sS]eventh\b|\b[eE]ighth\b|\b[nN]inth\b')

	if reType is None:
		return enREdict
	else:
		senREdict = {}
		for t in reType:
			senREdict.setdefault(Type_num[t], enREdict[Type_num[t]])
		return senREdict


# Chinese RE_with_Trie_Tree
def zhRE_d(reType):
	zhRE = str()

	zhREdict = {}
	zhREdict.setdefault(0,r'(([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})\s?年\s?[的]?)?[十\d]?[一二三四五六七八九十\d]\s?月\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号)|([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})\s?年的?\s?[十\d]?[一二三四五六七八九十\d]\s?月(\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号|號))?|[12][09]\d\d[- /.][0-3]?[0-9][- /.][0-3]?[0-9]|[0-3]?[0-9][- /.][0-3]?[0-9][- /.][12][09]\d\d|[12][019]\d{2}年|([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})年|[０１２３４５６７８９]{4}年?|[一二三四五六七八九十\d]{2,3}世[紀纪][一二三四五六七八九十\d]{2}年代|\d{2,3}年代|(一|二|三|四|五|六|七|八|九|十|十一|十二|\d+)月份?|([０１２３４５６７８９]{2}|\d\d|[一二三四五六七八九十]{1,3})日')
	zhREdict.setdefault(1,r'[0-2]?\d[:：][0-5][0-9](\s?[aApP]\.?[mM]\.?\b)?|([上下]午)?([0]?[1-9]|[1][012]|[2][0-4]|一|两|兩|二|三|四|五|六|七|八|九|十|十一|十二)(時|点钟|點鐘)半?[0-5]?[0-9]?([一|两|兩|二|三|四|五|六|七|八|九|十]+)?分?[0-5]?[0-9]?([一|两|兩|二|三|四|五|六|七|八|九|十]+)?秒?|星期[一二三四五六日]')
	zhREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	zhREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	zhREdict.setdefault(4,r'(((第?\d+([\,\./ ]\d+)*|\d+)(/M|/m)?號?(平方米)?|(\d+([．\,\./点點]\d+)*|[１２３４５６７８９０]+([．\,\.点點][１２３４５６７８９０]+)*|第?(壹|貳|叁|肆|伍|陸|柒|捌|玖|两|兩|一等|一、|二等?|三等?|四|五|六|七|八|九|十)+(([．点點](拾|佰|仟|壹|貳|叁|肆|伍|陸|柒|捌|玖|百|一|二|三|四|五|六|七|八|九|十|拾|零|几|幾|多)+)壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|十|拾|佰|仟|零|几|幾|多|十|百|千|万|萬|億|亿|兆)*)(多|拾|佰|仟|十|百|千|万|亿|萬|億|兆)*)+|第?[一十拾](([．点點](壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|拾|佰|仟|十|零|几|幾|多)+)壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|拾|佰|仟|十|零|几|幾|多|十|百|千|万|萬|億|亿|兆)+(多|十|百|千|万|亿|拾|佰|仟|萬|億|兆)*)|第(\d|[壹贰叁肆伍陸柒捌玖拾一二三四五六七八九十])+|乙方|甲方')
	
	if reType is None:
		return zhREdict
	else:
		szhREdict = {}
		for t in reType:
			szhREdict.setdefault(Type_num[t], zhREdict[Type_num[t]])
		return szhREdict


# Chinese RE_without_Trie_Tree
def zhRE(reType):
	zhRE = str()

	zhREdict = {}
	zhREdict.setdefault(0,r'(([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})\s?年\s?[的]?)?[十\d]?[一二三四五六七八九十\d]\s?月\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号)|([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})\s?年的?\s?[十\d]?[一二三四五六七八九十\d]\s?月(\s?[二三\d]?[十\d]?[一二三四五六七八九十\d]\s?(日|号|號))?|[12][09]\d\d[- /.][0-3]?[0-9][- /.][0-3]?[0-9]|[0-3]?[0-9][- /.][0-3]?[0-9][- /.][12][09]\d\d|[12][019]\d{2}年|([一二][一二三四五六七八九零][一二三四五六七八九零]{2}|1[789]\d{2}|2[0123]\d{2})年|[０１２３４５６７８９]{4}年?|[一二三四五六七八九十\d]{2,3}世[紀纪][一二三四五六七八九十\d]{2}年代|\d{2,3}年代|(一|二|三|四|五|六|七|八|九|十|十一|十二|\d+)月份?')
	zhREdict.setdefault(1,r'[0-2]?\d[:：][0-5][0-9](\s?[aApP]\.?[mM]\.?\b)?|([上下]午)?([0]?[1-9]|[1][012]|[2][0-4]|一|两|兩|二|三|四|五|六|七|八|九|十|十一|十二)(時|点钟|點鐘)半?[0-5]?[0-9]?([一|两|兩|二|三|四|五|六|七|八|九|十]+)?分?[0-5]?[0-9]?([一|两|兩|二|三|四|五|六|七|八|九|十]+)?秒?|星期[一二三四五六日]')
	zhREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	#zhREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	zhREdict.setdefault(3,r'(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?')
	zhREdict.setdefault(4,r'(((第?\d+([\,\./ ]\d+)*|\d+)(/M|/m)?[號|号]?(平方米)?|(\d+([．\,\./点點]\d+)*|[１２３４５６７８９０]+([．\,\.点點][１２３４５６７８９０]+)*|第?(壹|貳|叁|肆|伍|陸|柒|捌|玖|两|兩|一等|一、|二等?|三等?|四|五|六|七|八|九|十)+(([．点點](拾|佰|仟|壹|貳|叁|肆|伍|陸|柒|捌|玖|百|一|二|三|四|五|六|七|八|九|十|拾|零|几|幾|多)+)壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|十|拾|佰|仟|零|几|幾|多|十|百|千|万|萬|億|亿|兆)*)(多|拾|佰|仟|十|百|千|万|亿|萬|億|兆)*)+|第?[一十拾](([．点點](壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|拾|佰|仟|十|零|几|幾|多)+)壹|貳|叁|肆|伍|陸|柒|捌|玖|一|二|三|四|五|六|七|八|九|拾|佰|仟|十|零|几|幾|多|十|百|千|万|萬|億|亿|兆)+(多|十|百|千|万|亿|拾|佰|仟|萬|億|兆)*)|第(\d|[壹贰叁肆伍陸柒捌玖拾一二三四五六七八九十])+|乙方|甲方')
	zhREdict.setdefault(5,r'')
	if reType is None:
		return zhREdict
	else:
		szhREdict = {}
		for t in reType:
			szhREdict.setdefault(Type_num[t], zhREdict[Type_num[t]])
		return szhREdict


# Portuguese RE_with_Trie_Tree
def ptRE_d(reType):
	ptRE = str()

	ptREdict = {}
	ptREdict.setdefault(0,r'([0-2]?\d|3[01])( de )([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)( de )(\d{4}|\d{2})|([0-2]?\d|3[01])( de )([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)|([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)( de )(\d{4}|\d{2})|([aA]no|[Ee]m|[pP]ara) \d{4}|(dia )([0-2]?\d|3[01])|( de|[eE]m|[Pp]ara) ([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio |[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)(?!( de ))|de (1[789]\d{2}|2[0123]\d{2})')
	ptREdict.setdefault(1,r'\b([dD]omingo|[sS]egunda.feira|[tT]erça.feira|[qQ]uarta.feira|[sS]exta.feira|[sS]ábado|[qQ]uinta.feira)\b|\b(Segunda|Terça|Quarta|Sexta|Quinta)\b|(([Vv]inte e (um|uma|dois|duas|três|quatro)|[Uu]ma|[Dd]uas|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove) (hora(s)?|(e (um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|quatorze|quinze|dezesseis|dezessete|dezoito|dezenove|meia|sessenta|((vinte|trinta|quarenta|cinquenta) e (um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez))|vinte|trinta|quarenta|cinquenta))))|(([1-9]|1[0-9])|(2[0-4])) hora(s)?|(\d)+[Hh](\d)+|[0-2]?[0-9][, ]+[0-6][0-9] hora(s)?')
	ptREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	ptREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	ptREdict.setdefault(4,r'((((n.º )?\d+([\,\./ ]\d+)*|\d+)(/m|/M)?(.º|.ª)?( m2)?([\s\-]([Dd]ez|[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))*|\b(([Dd](ois|uas)|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez|[Cc](em|ento)|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove|[Vv]inte|[tT]rinta|[Qq]uarenta|[Cc]inquenta|[sS]essenta|[sS]etenta|[Oo]itenta|[nN]oventa|(duzent|trezent|quatrocent|quinhent|seiscent|setecent|oitocent|novecent)[oa]s)\b((\s|, )([Dd]ez|[Cc](em|ento)|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove|[Vv]inte|[tT]rinta|[Qq]uarenta|[Cc]inquenta|[sS]essenta|[sS]etenta|[Oo]itenta|[nN]oventa|(duzent|trezent|quatrocent|quinhent|seiscent|setecent|oitocent|novecent)[oa]s|[Mm]il|e|[pP]onto|[Uu]m(a)?|[Dd](ois|uas)|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez)\b)*)([\W]([Dd]ez|[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))*)+|\b[uU]m(a)?(\s([Dd]ez[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))+)|((\s|\b)([Pp]rimeir|[Ss]egund|[Tt]erceir|[Qq]uart|[Qq]uint|[Ss]ext|[Ss]étim|[Oo]itav|[Nn]on|[Dd]écim|[Vv]igésim|[Tt]rigésim|[Qq]uadragésim|[Qq]uinquagésim|[Ss]exagésim|[Ss]eptuagésim|[Oo]ctogésim|[Nn]onagésim|[Cc]entésim)(o|a)s?\b)+')
	
	if reType is None:
		return ptREdict
	else:
		sptREdict = {}
		for t in reType:
			sptREdict.setdefault(Type_num[t], ptREdict[Type_num[t]])
		return sptREdict


# Portuguese RE_without_Trie_Tree
def ptRE(reType):
	ptRE = str()

	ptREdict = {}
	ptREdict.setdefault(0,r'([0-2]?\d|3[01])( de )([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)( de )(\d{4}|\d{2})|([0-2]?\d|3[01])( de )([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)|([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio|[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)( de )(\d{4}|\d{2})|([aA]no|[Ee]m|[pP]ara) \d{4}|(dia )([0-2]?\d|3[01])|( de|[eE]m|[Pp]ara) ([jJ]aneiro|[fF]evereiro|[mM]arço|[aA]bril|[mM]aio |[jJ]unho|[jJ]ulho|[aA]gosto|[sS]etembro|[oO]utubro|[nN]ovembro|[dD]ezembro)(?!( de ))|de (1[789]\d{2}|2[0123]\d{2})')
	ptREdict.setdefault(1,r'\b([dD]omingo|[sS]egunda.feira|[tT]erça.feira|[qQ]uarta.feira|[sS]exta.feira|[sS]ábado|[qQ]uinta.feira)\b|\b(Segunda|Terça|Quarta|Sexta|Quinta)\b|(([Vv]inte e (um|uma|dois|duas|três|quatro)|[Uu]ma|[Dd]uas|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove) (hora(s)?|(e (um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|quatorze|quinze|dezesseis|dezessete|dezoito|dezenove|meia|sessenta|((vinte|trinta|quarenta|cinquenta) e (um|uma|dois|duas|três|quatro|cinco|seis|sete|oito|nove|dez))|vinte|trinta|quarenta|cinquenta))))|(([1-9]|1[0-9])|(2[0-4])) hora(s)?|(\d)+[Hh](\d)+|[0-2]?[0-9][, ]+[0-6][0-9] hora(s)?')
	ptREdict.setdefault(2,r'[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)*')
	#ptREdict.setdefault(3,r'(([A-Za-z]{3,9}:(?:\/\/)?)([A-Za-z0-9\-]+)|(?:www))(\.[\!\-;:&=\+\$,\w\+~%\/]+)+')
	ptREdict.setdefault(3,r'(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?')
	ptREdict.setdefault(4,r'((((n.° |n.º )?\d+([\,\./ ]\d+)*|\d+)(/m|/M)?(.º|.ª|.°)?( m2)?([\s\-]([Dd]ez|[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))*|\b(([Dd](ois|uas)|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez|[Cc](em|ento)|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove|[Vv]inte|[tT]rinta|[Qq]uarenta|[Cc]inquenta|[sS]essenta|[sS]etenta|[Oo]itenta|[nN]oventa|(duzent|trezent|quatrocent|quinhent|seiscent|setecent|oitocent|novecent)[oa]s)\b((\s|, )([Dd]ez|[Cc](em|ento)|[Oo]nze|[Dd]oze|[Tt]reze|[Qq]uatorze|[Qq]uinze|[Dd]ezesseis|[Dd]ezessete|[Dd]ezoito|[Dd]ezenove|[Vv]inte|[tT]rinta|[Qq]uarenta|[Cc]inquenta|[sS]essenta|[sS]etenta|[Oo]itenta|[nN]oventa|(duzent|trezent|quatrocent|quinhent|seiscent|setecent|oitocent|novecent)[oa]s|[Mm]il|e|[pP]onto|[Uu]m(a)?|[Dd](ois|uas)|[Tt]rês|[Qq]uatro|[Cc]inco|[Ss]eis|[Ss]ete|[Oo]ito|[Nn]ove|[Dd]ez)\b)*)([\W]([Dd]ez|[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))*)+|\b[uU]m(a)?(\s([Dd]ez[Cc](em|ento)|[mM]ilh(ão|õe)(s)?|[mM]il|[bB]ili(ão|õe)(s)?))+)|((\s|\b)([Pp]rimeir|[Ss]egund|[Tt]erceir|[Qq]uart|[Qq]uint|[Ss]ext|[Ss]étim|[Oo]itav|[Nn]on|[Dd]écim|[Vv]igésim|[Tt]rigésim|[Qq]uadragésim|[Qq]uinquagésim|[Ss]exagésim|[Ss]eptuagésim|[Oo]ctogésim|[Nn]onagésim|[Cc]entésim)(o|a)s?\b)+')
	ptREdict.setdefault(5,r'')
	if reType is None:
		return ptREdict
	else:
		sptREdict = {}
		for t in reType:
			sptREdict.setdefault(Type_num[t], ptREdict[Type_num[t]])
		return sptREdict


# ------------------------End------------------------

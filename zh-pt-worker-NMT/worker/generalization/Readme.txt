**version 4.1.4:
1.Add regex of Portuguese.
2.Support zh/en zh/pt and en/pt bilingual languages.
3.Update the regex of en.


**version 4.1.3:
1. Add a option '-n', use this option can omit and not replace the pattern which cannot alignment to another pattern. 
2. Complete the option '-f', use this option to launch the program by multiprocessing
3. Fix the regex error bug.


**To launch Patter.py, the version of python must be great than python 2.7


**Launch command
python Patter.py -i filename [-o outputFilename] [-l bilexiconFilename] [-s languageType] [-t patternType] [-v 0/1/2] [-p patternizedSentence] [-n] [-d] [-m] [-f numberOfProcess]


**To check the options usage detail, can use the command
python Pattern.py -h


**To add new language, pattern type or change the Regular Expression,
**you can update the content of RE_Base.py by following the steps inside the program.


**Before update the Regular Expression, if you want to check is it suitable or not, 
**you can use RE_test.py to test your Regular Expression.
**To test the RE, you need to open the program and type the RE to the assign place.


**The alignment function in the Pattern.py is not work well, 
**and there are some problems for bilexicon parts.
**I feel sorry that I have not a good solution to fix these problems.


#####Example#####
--------------case 1-----------------
python Patter.py -i filename

程序自動寻找filename.en, filename.zh, 然后输出filename.pat.en, filename.pat.zh, filename.en-zh (第二种提取双語词汇的格式)。注：如果没有提供指定路徑，以使用当前的路徑。

--------------case 2-----------------
python Patter.py -i inputFilename -o outputFilename

输出outputFilename.pat.en, outputFilename.pat.zh, outputFilename.en-zh，输入如上述。

--------------case 3-----------------
python Patter.py  -o outputFilename -l bilingualFilename -i inputFilename

输出为指定的outputFilename.en, outputFilename zh, bilingualFilename.en-zh，输入如上述。

--------------case 4-----------------
python Patter.py  -o outputFilename -l bilingualFilename -i inputFilename -m

if -m is given, 输出 bilingualFilename.m.en-zh, others are similar as above

--------------case 5-----------------
python Patter.py  -o outputFilename -i inputFilename -m

if -m is given, alternative format (refer to end of this document) 输出 outputFilename.m.en-zh, others are similar as above

--------------case 6-----------------
python Patter.py  -o outputFilename -i inputFilename -s en

-s represents single language file, followed by the language, example: -s en

--------------case 7-----------------
python Patter.py  -o outputFilename -i inputFilename -p n

if -p is given, 输出4个文档： outputFilename.p.en, outputFilename.p.zh, outputFilename.u.en, outputFilename.u.zh, others are similar as above

--------------case 8-----------------
python Patter.py  -o outputFilename -i inputFilename -v 0/1/2

Option 0: [-v 0]
13 ||| 7 ||| 2 620 0 0 0 54 9.59 ||| 262 1 3 540 null null null 
There are @NUM@,@NUM@,@NUM@@NUM@@NUM@ square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than @NUM@ billion yuan ($@NUM@ billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有@NUM@万平方公里的土地退化，占国土面积的@NUM@/@NUM@，每年带来的经济损失超过@NUM@亿元。

Option 1: [-v 1]
13 ||| 7 ||| 2 620 0 0 0 54 9.59 ||| 262 1 3 540 null null null
There are 2,620,000 square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than 54 billion yuan ($9.59 billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有262万平方公里的土地退化，占国土面积的1/3，每年带来的经济损失超过540亿元。

Option 2: [-v 2]
13 ||| 7 ||| 2 620 0 0 0 54 9.59 ||| 262 1 3 540 null null null 
There are @NUM@,@NUM@,@NUM@@NUM@@NUM@ square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than @NUM@ billion yuan ($@NUM@ billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有@NUM@万平方公里的土地退化，占国土面积的@NUM@/@NUM@，每年带来的经济损失超过@NUM@亿元。
There are 2,620,000 square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than 54 billion yuan ($9.59 billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有262万平方公里的土地退化，占国土面积的1/3，每年带来的经济损失超过540亿元。

For alternative bilexicon format: [-m -v 2]
54 ||| 20 ||| 1991
54 ||| 1991 ||| 20
54 ||| 1991 ||| 1991
54 ||| 130 ||| 130
There are @NUM@,@NUM@,@NUM@@NUM@@NUM@ square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than @NUM@ billion yuan ($@NUM@ billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有@NUM@万平方公里的土地退化，占国土面积的@NUM@/@NUM@，每年带来的经济损失超过@NUM@亿元。
There are 2,620,000 square kilometers of land degraded by desertification in China, which makes up one-third of the national territory and causes more than 54 billion yuan ($9.59 billion) of economic loss a year, according to the State Forestry Administration.
根据国家林业局数据统计，由于沙漠化，中国有262万平方公里的土地退化，占国土面积的1/3，每年带来的经济损失超过540亿元。
57 ||| 15 ||| 150
57 ||| 15 ||| 150
57 ||| 2015 ||| 2015


- For invalid inputs, display the instruction/help
- Show progression:
	....5000
	....10000
	....15000
	...





Made by: Don Ku

#encoding=utf-8
# this program is used to check the RE.

import sys
import re

if __name__=='__main__':

	# ******Type the test Regular expression here******
	RE = r''

	count = 0

	# Main Program
	if len(sys.argv) == 1 or len(sys.argv) > 5:
		print 'Launch format:'
		print "python RE_test.py input_file [output_file]"
	else:	
		# open input file
		try:
			infile = open(sys.argv[1],'r')
		except:
			print "Input file \"" + sys.argv[1] + "\" not exist."
			quit()

		HaveOutPut = False
		lineNo = 0

		# open output file if there are
		if len(sys.argv) >= 3 and sys.argv[2][0] != '-':
			outfile = open(sys.argv[2],'w')
			HaveOutPut = True

		# get the line one by one(While Loop)
		while True:
			line = infile.readline()
			
			# break the loop if there are no more line
			if not line:
				infile.close()
				if HaveOutPut:
					outfile.close()
				break
			
			line = line.decode('utf8')
			lineNo = lineNo + 1
			conform = False
			ext = []

			# find the line that it match with the __RE__
			recompi = re.compile(RE.decode('utf8'))
			match = recompi.finditer(line)

			for word in match:
				conform = True
				ext.append(word.group().encode('utf8'))
			
			# print the match line with different ways
			if conform:
				if HaveOutPut:	
					outfile.write("--line_"+ str(lineNo)+ "--: ( ")
					for i in ext:
						outfile.write(i)
						outfile.write(' ')
						count = count + 1
					outfile.write(")\n")
					outfile.write(line.encode('utf8'))
				else:
					print '--line_' + str(lineNo) + '--:'
					for i in ext:
						print i + ' |||',
					print '\n'
					print line.encode('utf8')
					count = count + len(ext)

			if HaveOutPut:
				if lineNo % 100 == 0:
					if lineNo % 1000 == 0:
						sys.stdout.write('%d' % lineNo)
					else:
						sys.stdout.write('.')

		print "\nThere are", count, "items match the RE."
		print "Done."	

	#End Program
		

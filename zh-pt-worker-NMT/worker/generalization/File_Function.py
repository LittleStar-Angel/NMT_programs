from subprocess import call

def cut_f(f_name, num_of_parts):
	num_lines = sum(1 for line in open(f_name))

	inifile = open(f_name,'r')

	num_part = num_of_parts

	lines_per_part =  num_lines / num_part

	if lines_per_part <= 100:
		print 'Length of file is too small, cannot cut any more.'
		quit()

	print 'Cutting file: ' + f_name + ' to ' + str(num_of_parts) + ' parts.'

	for i in range(1, num_of_parts + 1):
		f = open(f_name+'.'+str(i),'w')
	
		count = 0
	
		if i == 1:
			line = inifile.readline()
	
		while (count <= lines_per_part and i != num_of_parts) or (i == num_of_parts):
			f.write(line)
			count = count + 1
			line = inifile.readline()
			if not line:
				break

		f.close()
	
	inifile.close()

	print 'Finished cutting.'

	return lines_per_part


def del_parts_f(f_name, num_of_parts):
	for i in range(1, num_of_parts + 1):
		part_name = f_name+'.'+str(i)
		
		try: 
			f = open(part_name,'r')
		except:
			print 'No file: ' + part_name

		f.close()
		
		call(['rm',part_name])

	print 'Cutted file deleted Completed.'



def merge_f(f_name, num_of_parts):
	try:
		f = open(f_name,'r')
	except:
		f = None
		pass

	if f != None:
		keep_doing = raw_input('File \''+f_name+'\' is exsit, do you want to cover it?(y/n): ')
		while keep_doing != 'y' and keep_doing != 'n':
			keep_doing = raw_input('File \''+f_name+'\' is exsit, do you want to cover them(y/n): ')
	
		if keep_doing == 'n':
			return

	f = open(f_name,'w')
	
	for i in range(1, num_of_parts + 1):
		try:
			part_f = open(f_name+'.'+str(i))
		except:
			print 'No file: ' + f_name+'.'+str(i)

		while True:
			line = part_f.readline()
			
			if not line:
				break

			f.write(line)

		part_f.close()

	f.close()

	print 'Mert completed.'

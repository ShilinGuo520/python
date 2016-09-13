#!/usr/bin/env python

	
def menu():
	print '***************************'
	print '<1> input'
	print '<2> output'

back_data = []

def input_func():
	name = raw_input("input you name:")
	num = int(raw_input("input you number:"))
	sex = raw_input("input you sex:")
	scor = int(raw_input("input you s:"))
	ret = [name, num, sex, scor]
	back_data.append(ret)
	print 'input done'
	return ret

def output_func():
	pri = back_data[0]
	print pri[0]
	print pri[1]
	print pri[2]


if __name__=='__main__':
	menu()
	while 1 :
		choose = raw_input("choose:")
		if choose == 'q' or choose == 'Q':
			print 'you choose exit'
			exit()
		elif choose == '1':
			print 'you choose 1'
			input_func()
		elif choose == '2':
			print 'you choose 2'
			output_func()
		else :
			print 'error'
                    

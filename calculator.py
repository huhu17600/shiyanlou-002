#!/usr/bin/env python3

import sys

def calculate(wages):
	income = wages
	wages = wages - wages * 0.165 - 3500
	if(wages > 80000):
		wages = wages * 0.45 - 13505
	elif(wages > 55000):
		wages = wages * 0.35 - 5505
	elif(wages > 35000):
		wages = wages * 0.3 - 2755
	elif(wages > 9000):
		wages = wages * 0.25 - 1005
	elif(wages > 4500):
		wages = wages * 0.2 - 555
	elif(wages > 1500):
		wages = wages * 0.1 - 105
	elif(wages > 0 ):
		wages = wages * 0.03
	else:
		wages = 0
	return income - wages - income * 0.165


try:
	if(len(sys.argv[1:])>=1):
		for arg in sys.argv[1:]:
			Str = arg.split(':')
			if(not (isinstance(int(Str[0]),int) and isinstance(int(Str[1]),int))):
				raise
		for arg in sys.argv[1:]:
			Str = arg.split(':')
			worker_ID = int(Str[0])
			Para = int(Str[1])
			result = calculate(Para)
			print("{}:{:.2f}".format(worker_ID,result))
	else:
		raise
except:
	print("Parameter Error")

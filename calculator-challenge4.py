#!/usr/bin/env python3

from multiprocessing import Process, Queue, Lock
import sys
import os.path
queue1 = Queue()
queue2 = Queue()
def queue1_f1():
	with lock:
		print("here is queue1_f1")
		args = sys.argv[1:]
		if(len(args)<6):
			raise
		indexC = args.index('-c')
		indexD = args.index('-d')
		indexO = args.index('-o')
		if((indexC%2)or(indexD%2)or(indexO%2)):
			raise
		if(not(os.path.isfile(args[indexC + 1]))):
			raise
#		if(not(os.path.exists(args[indexC + 1]))):
 #                       raise
		if(not(os.path.isfile(args[indexD + 1]))):
                        raise
#		if(not(os.path.exists(args[indexD + 1]))):
#                        raise
#		if(not(os.path.dirname(args[indexO + 1]))):
#			raise
		test_data = []
		user_data = []
		with open(args[indexC + 1]) as file1:
			lines = file1.readlines()
			for line in lines:
				Str = line.split('=')
				test_data.append(Str[0].strip())
				test_data.append(Str[1].strip(' \n'))
	#               print(test_data)
		with open(args[indexD + 1]) as file2:
			lines = file2.readlines()
			for line in lines:
				Str = line.split(',')
				user_data.append(Str[0].strip())
				user_data.append(Str[1].strip(' \n'))
	#                print(user_data)

		queue1.put(test_data)
		queue1.put(user_data)

def queue1_f2():
	with lock:
		print('here is queue1_f2')
		data1 = queue1.get()
		data2 = queue1.get()
		result_data = calculator(data1,data2)
		queue2.put(result_data)

def queue2_f1():
	with lock:
		print('here is queue2_f1')
		args = sys.argv[1:]
		indexO = args.index('-o')
		data = queue2.get()
		with open(args[indexO + 1],'w') as file3:
			file3.write('')
		with open(args[indexO + 1],'a') as file3:
			for item in data:
				file3.write(item + '\n')
				 
def calculator(a,b):
	result = []
	JiShuL = a[a.index('JiShuL') + 1]
	JiShuH = a[a.index('JiShuH') + 1]
	YangLao = a[a.index('YangLao') + 1]
	YiLiao = a[a.index('YiLiao') + 1]
	ShiYe = a[a.index('ShiYe') + 1]
	GongShang = a[a.index('GongShang') + 1]
	ShengYu = a[a.index('ShengYu') + 1]
	GongJiJin = a[a.index('GongJiJin') + 1]
	num = len(b)//2
	for i in range(num):
		percentage = float(YangLao)+float(YiLiao)+float(ShiYe)+float(GongShang)+float(ShengYu)+float(GongJiJin)
			
		income =float(b[i*2+1])
		if(income<float(JiShuL)):
			socialsecurity = float(JiShuL) * percentage
			wages = income - float(JiShuL) * percentage - 3500
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
			income = income - wages - float(JiShuL) * percentage
		elif(income>float(JiShuH)):
			socialsecurity = float(JiShuH) * percentage
			wages = income - float(JiShuH) * percentage - 3500
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
			income = income - wages - float(JiShuH) * percentage
		else:
			socialsecurity = income * percentage
			wages = income - income * percentage - 3500
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
			income = income - wages - income * percentage
		socialsecurity = "{:.2f}".format(socialsecurity)
		wages = "{:.2f}".format(wages)
		income = "{:.2f}".format(income)
		para = [b[i*2],b[i*2+1],str(socialsecurity),str(wages),str(income)]
		para = ','.join(para)
		result.append(para)
	return result

if __name__ == '__main__':

	try:
		lock = Lock()
		procs = []

		procs.append(Process(target=queue1_f1))
		procs.append(Process(target=queue1_f2))
		procs.append(Process(target=queue2_f1))

		for p in procs:
			p.start()
			p.join()

	except:
		print('Parameter Error')	

#!/usr/bin/env python3
from multiprocessing import Process, Queue, Lock
import configparser,getopt
from datetime import date, datetime, timedelta
import sys
import os.path
queue1 = Queue()
queue2 = Queue()
def queue1_f1():
	with lock:
#		print("here is queue1_f1")
		ops = getopt.getopt(sys.argv[1:],"hC:c:d:o:",["help"])
		cityname = ''
		configfile = ''
		userdata = ''
		resultdata = ''		
		for op in ops[0]:
			if(op):
				if(str(op[0])=='-C'):
					cityname = str(op[1]).upper()
				else:
					cityname = 'DEFAULT'
				if(str(op[0])=='-c'):
					configfile = str(op[1])
				if(str(op[0])=='-d'):
					userdata = str(op[1])
				if(str(op[0])=='-o'):
					resultdata = str(op[1])
		conf = configparser.ConfigParser()
		conf.read(configfile)

		kvs = conf.items(cityname)
		test_data = []
		for kv in kvs:
			if(str(kv[0])=='JiShuL'.lower()):
				JiShuL = float(kv[1])
				test_data.append('JiShuL')
				test_data.append(JiShuL)
			if(str(kv[0])=='JiShuH'.lower()):
				JiShuH = float(kv[1])
				test_data.append('JiShuH')
				test_data.append(JiShuH)
			if(str(kv[0])=='YangLao'.lower()):
				YangLao = float(kv[1])
				test_data.append('YangLao')
				test_data.append(YangLao)
			if(str(kv[0])=='YiLiao'.lower()):
				YiLiao = float(kv[1])
				test_data.append('YiLiao')
				test_data.append(YiLiao)
			if(str(kv[0])=='ShiYe'.lower()):
				ShiYe = float(kv[1])
				test_data.append('ShiYe')
				test_data.append(ShiYe)
			if(str(kv[0])=='GongShang'.lower()):
				GongShang = float(kv[1])
				test_data.append('GongShang')
				test_data.append(GongShang)
			if(str(kv[0])=='ShengYu'.lower()):
				ShengYu = float(kv[1])
				test_data.append('ShengYu')
				test_data.append(ShengYu)
			if(str(kv[0])=='GongJiJin'.lower()):
				GongJiJin = float(kv[1])
				test_data.append('GongJiJin')
				test_data.append(GongJiJin)
		
		
		user_data = []
		
		with open(userdata) as file2:
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
#		print('here is queue1_f2')
		data1 = queue1.get()
		data2 = queue1.get()
		result_data = calculator(data1,data2)
		queue2.put(result_data)

def queue2_f1():
	with lock:
#		print('here is queue2_f1')
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
		t = datetime.now()
		now = str(datetime.strftime(t, '%Y-%m-%d %H:%M:%S'))
		para = [b[i*2],b[i*2+1],str(socialsecurity),str(wages),str(income),now]
		para = ','.join(para)
		result.append(para)
	return result
	
def usage():
	print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
	
if __name__ == '__main__':
	
	try:
		ops,args = getopt.getopt(sys.argv[1:],"hC:c:d:o:", ["help"])
		for o,a in ops:
			if o in ("-h", "--help"):
				usage()
				sys.exit(0)
			if o in ("-c","-d"):
				if(not(os.path.isfile(a))or(not(os.path.exists(a)))):
					raise getopt.GetoptError('')
			if o in ("-C"):
				if(str(a).upper()) not in ('CHENGDU','BEIJING'):
					raise getopt.GetoptError('')
#			if o in ("-o"):
#				if():
#					raise getopt.GetoptError('')
				
		lock = Lock()
		procs = []

		procs.append(Process(target=queue1_f1))
		procs.append(Process(target=queue1_f2))
		procs.append(Process(target=queue2_f1))

		for p in procs:
			p.start()
			p.join()
	except getopt.GetoptError:  
		print("getopt error!");  
		usage();  
		sys.exit(); 

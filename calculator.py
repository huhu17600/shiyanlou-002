#!/usr/bin/env python3

class Config(object):
	def __init__(self):
		self._config = {}
	def set_config(self,value):
		Str = value.split('=')
#		print(Str[0].strip(),Str[1].strip(' /n'))
		self._config[Str[0].strip()] = Str[1].strip(' \n')
	def get_config(self,value):
		return self._config[value]
class UserData(object):
	def __init__(self):
		self._userdata = {}
	def set_userdata(self,value):
		Str = value.split(',')
		self._userdata[Str[0].strip()] = Str[1].strip(' \n')
	def get_userdata(self,value):
		return self._userdata[value]
	def calculate(self,JiShuL,JiShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin):
		for key,value in self._userdata.items():
			percentage = float(YangLao)+float(YiLiao)+float(ShiYe)+float(GongShang)+float(ShengYu)+float(GongJiJin)
			
			income =float(value)
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
			para = [key,value,str(socialsecurity),str(wages),str(income)]
			self._userdata[key] = ','.join(para)
	def dumptofile(self):
		Str = []
		for key in self._userdata:
			Str.append(self._userdata[key])
		return Str
if __name__ == '__main__':
	import sys
	test = Config()
	User = UserData()
	args = sys.argv[1:]
	indexC = args.index('-c')
	indexD = args.index('-d')
	indexO = args.index('-o')
	with open(args[indexC + 1]) as file1:
		lines = file1.readlines()
		for line in lines:
			test.set_config(line)
	JiShuL = test.get_config('JiShuL')
	JiShuH = test.get_config('JiShuH')
	YangLao = test.get_config('YangLao')
	YiLiao = test.get_config('YiLiao')
	ShiYe = test.get_config('ShiYe')
	GongShang = test.get_config('GongShang')
	ShengYu = test.get_config('ShengYu')
	GongJiJin = test.get_config('GongJiJin')
	with open(args[indexD + 1]) as file2:
		users = file2.readlines()
		for user in users:
			User.set_userdata(user)
		
		User.calculate(JiShuL,JiShuH,YangLao,YiLiao,ShiYe,GongShang,ShengYu,GongJiJin)
	with open(args[indexO + 1],'a') as file3:
		items = User.dumptofile()
		for item in items:
			file3.write(item)
	
	with open(args[indexO + 1]) as file:
		file.readlines()

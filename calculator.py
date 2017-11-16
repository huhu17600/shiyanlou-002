#!/usr/bin/env python3

class Config(object):
	def __init__(self):
		self._config = {}
	def set_config(self,value):
		Str = value.split(':')
		self._config[Str[0].strip()] = Str[1].strip()
	def get_config(self,value):
		return self._config[value]
class UserData(object):
	def __init__(self):
		self._userdata = {}
	def set_userdata(self,value):
		Str = value.split(',')
		self._userdata[Str[0].strip()] = Str[1].strip()
	def get_userdata(self,value):
		return self._userdata[value]
	def calculate(self):
		for key,value in self._userdata:
			income = value
			wages = value
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
			income = income - wages - income * 0.165
			print("{}:{:.2f}".format(key,income))

if __name__ = '__main__':
import sys


#!/usr/bin/python

import logging

'''
	filename:存放目录
	filemode:打开文件的模式
	level:打印日志的级别
	format:打印日志的格式
'''
logging.basicConfig(filename='/home/rds-user/t.log', filemode = 'a',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('start of program')

def factorial(n):
	logging.debug('start of factorial (%s%%)' % (n))
	total = 1
	for i in range(n+1):
		total *=i
		logging.debug('i is ' + str(i) + ', total is ' + str(total) )
	
	logging.debug('end of factorial (%sSS)' % (n))
	return total

factorial(5)

logging.debug('end of program')
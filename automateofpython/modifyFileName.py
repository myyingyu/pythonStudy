#!/usr/bin/python
# coding=utf-8

import re
import sys
import os
import shutil

'''
	功能：修改为文件名，将美国风格的日期(MM-DD-YYYY)修改为欧洲风格的日期(DD-MM-YYYY)
	目的：熟悉对文件名修改，移动等操作
'''

def is_exist_america_data(data_str):
	'''
		1、利用re的compile创建一个匹配对象dataRegex
		2、利用dataRegex的findadll方法发现字符串中是否存在符合的匹配
		dataRegex = re.compile(r'^(.*)(([0|1|2|3]?\d)-([0|1]?\d)-(\d\d\d\d))(.*)$')--有问题
		 dataRegex.findall('zhaoyan 21-10-2012 zhoayan')
		结果：[('zhaoyan 2', '1-10-2012', ' zhoayan')]--因为正则表达式是贪心算法
		解决：在前端加一个？表示是非贪心
	'''
	#dataRegex = re.compile(r'^(.*?)([0|1|2|3]?\d-[0|1]?\d-\d\d\d\d)(.*)$')
	dataRegex = re.compile(r'^(.*?)([0|1|2|3]?\d)-([0|1]?\d)-(\d\d\d\d)(.*)$') #[('zhaoyan is ', '23', '10', '2013', ' hel')]
	if data_str != None:
		result = dataRegex.search(data_str)
	else:
		raise Exception('parameter is not!')
	
	return result


def generator_new_filename(fileName):
	'''
		修改文件的名字
		[('zhaoyan is ', '23', '10', '2013', ' hel')]
		group(1): brfore string
		group(2): month
		group(1): day
		group(1): year
		group(1): after string
	'''
	if fileName != None:
		dataPattern = is_exist_america_data(fileName)
		if dataPattern != None:
			newFileName = '{0}{1}-{2}-{3}{4}'.format(dataPattern.group(1), 
						  dataPattern.group(3),
						  dataPattern.group(2),
						  dataPattern.group(4), 
						  dataPattern.group(5))
					 	  
			return newFileName
		else:
			print "this is filename don't hvae data!"
	else:
		raise Exception("file is not exist!")


	
def get_filename_from_path(filePath):
	'''
		从路径上获取所有文件
	'''
	files = []
	if os.path.isdir(filePath):
		 for f in os.listdir(filePath):
			if os.path.isfile(f):
				files.append(f)
	else:
		raise Exception("parameter isn't path!")
	return files	

def main():
	
	print 'start'
	#用户需要传入路径
	if len(sys.argv) < 2:
		print 'you must have 2 parameter!'
	
	#找出路径上所有的文件
	files = get_filename_from_path(sys.argv[1])
	
	if len(files) != 0:
		for file in files:
			#是否存在带有美国的文件，存在的话修改成欧洲日期
			exist_data  = is_exist_america_data(file)
			if exist_data != None:
				newFileName = generator_new_filename(file)
				#将文件修改新的名字名字
				print 'new'
				shutil.move(file, newFileName)
	print 'end'			
	
main()
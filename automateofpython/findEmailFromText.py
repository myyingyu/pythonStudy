
#!/usr/bin/python

import re
import os
import sys
import pprint

'''
    this function is used to find all email and phone in text
'''


def get_file_object(filePath):
    '''
        1、使用open方法读取路径上的文件，返回一个file对象；
        2、调用File对象的的read方法读取文件中的内容；
    '''
    if os.path.isfile(filePath):
        with open(filePath) as f:
            text = f.read()
    else:
        raise Exception('you must input correct file path!')
    return text

def get_email__from_text(text):
    '''
        1、使用compile创建Regex对象
        2、使用Regex对象的findall方法从文本中查找字符串
    '''
    emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{3,4}))', re.VERBOSE)
    match = emailRegex.findall(text)
    #pprint.pprint(match)
    return  match



def main():
    if len(sys.argv)<2:
        print 'you must input 2 args'
    else:
        str_from_file = get_file_object(sys.argv[1])
        #print  str_from_file
        result = get_email__from_text(str_from_file)
    pprint.pprint(result)

main()
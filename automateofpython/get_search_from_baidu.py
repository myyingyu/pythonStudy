#!/usr/bin/python

import requests
import bs4
import webbrowser

'''
	功能：
	1、使用requests和BeautifulSoup对网站中的源码进行解析获取对应的结果；
	2、使用webbrowser打开已经存在的网页;
'''
	
def get_search_url(search_val):
	'''
		根据搜索的内容生成一个百度请求的url
	'''
	if search_val:
		return r'http://www.baidu.com/s?wd=' + ' '.join(search_val)
	else:
		raise Exception('please input search content!')

def get_result_url(url):
	'''
		1、对requests的结果进行解析，这里要注意html.parser，如果没有可能会报错
		2、bs4中的select的使用,多多接触才能掌握
		3、根据请求码，返回不同的信息
	'''
	req = requests.get(url)
	if req.ok :
		sb = bs4.BeautifulSoup(res.text, "html.parser")
		elems = sb.select(r'.t a')
		for elem in elems:
			str(elem)
			get_href = elem.get('href')
			result.append(get_href)
		return req.status_code, result
	else:
		return req.status_code, 'url is error!'

def open_brower(urls):
	'''
		使用webbrowser打开指定的url,但在游览器的选择上，没有做任何事
	'''
	numopen = min(5, len(urls))
	for i in range(numopen):
		webbrowser.open(urls[i])

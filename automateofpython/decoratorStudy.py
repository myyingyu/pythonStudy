#!/usr/bin/python
# coding = utf-8

'''
	目的：主要是了解python中的装饰器是什么
	理解：感觉装饰器有点像springmvc中的aop的前后置通知；
	下面有三个例子，前两个效果相同：1、不使用装饰器的情况；2、使用装饰器的例子；3、如何为装饰的函数传递参数；
'''

'''
	函数
'''

#1、不使用装饰器
def sandwich():
    print 'breef'


def bread(func):
    def tt():
        print "<--------start-------->"
        func()
        print "<---------end -------->"
    return tt


bread(sandwich)()


#2、使用简单装饰器的函数
def bread(func):
    def tt():
        print "< ---- start decorator ------------>"
        func()
        print "<------ end decorator -------------->"
    return tt

@bread
def sandwich():
    print "breef"

sandwich()

#3、为装饰器函数传递参数
def check_parameter(func):
    def wrapper(*args, **kwargs):
        print "<------test parameter ------>"
        print func.__name__, args, kwargs
        func(*args, **kwargs)
    return wrapper


@check_parameter
def t(username, passwd):
    print "username : {0}, password : {1}".format(username, passwd)

t('zhaoyan', 'helloword')


'''
	注意事项：
	1、函数属性的变化
	2、使用inspect获取函数参数---inspect.getcallargs()
	3、多个装饰器的顺序---由近及远
	4、给装饰器传递参数--a、内层函数的参数是被装饰函数的参数，即wrapper中的args和kwargs是给func函数的参数；b、外层函数的参数是被装饰的函数，即check_parameter中的func的参数；
'''
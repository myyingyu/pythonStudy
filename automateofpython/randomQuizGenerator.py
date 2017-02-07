#!/usr/bin/python
# coding=utf-8
# coding=utf-8是用来处理文件中的中文，如果没有会报错

import random


#功能：是根据省会自动生成几套不同的试卷
#目的：为了练习对文件的操作

#建立一个字典，key表示一个省，key对应的value表示该省的省会
capitals = {'jiangsu': 'nanjing', 'zhejiang':'hangzhou', 'shanghai':'shanghai', 'anhui':'hefei', 'shanghan':'qingdao'}

for quizNum in range(3):
	#使用open方法以写的方式打开一个文件，quizFile为试卷，answerKeyFile为该份试卷对应的答案
	quizFile = open('capitalsquiz{0}.txt'.format(quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers{0}.txt'.format(quizNum + 1), 'w')
	
	#试卷的开头
	quizFile.write('Name :\n\n Date:\n\n Period: \n\n')
	quizFile.write((' '*20) + 'Sate Capitals Quiz (Form {0})'.format(quizNum + 1))
	quizFile.write('\n\n')
	
	#根据省会的key随机生成一组序列
	states = list(capitals.keys())
	random.shuffle(states)
	
	#生成该份试卷
	for questionNum in range(5):
		#获取该省的正确省会
		correctAnswer = capitals[states[questionNum]]
		#print 'correctAnswer is {0}'.format(correctAnswer)
		#随机生成错误选择
		wrongAnswers = list(capitals.values())
		#print 'wrongAnswers is {0}'.format(wrongAnswers)
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = [correctAnswer] + wrongAnswers
		random.shuffle(answerOptions)

		#向文本写入题目
		quizFile.write('{0}. what is the capital of {1}? \n'.format(questionNum+1, states[questionNum]))
		for i in range(4):
			quizFile.write('{0}. {1}\n'.format('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		answerKeyFile.write('{0}. {1}\n'.format(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
	
	#关闭打开的文件
	quizFile.close()
	answerKeyFile.close()
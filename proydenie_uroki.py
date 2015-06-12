#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author: CanonPRO
@Date: 2015-6-12
"""

sps = {}

yourname = ("Имя: ")
yourfamily = ("Фамилия: ")
yourage = ("Вам лет: ")
yourcity = ("Вы из: ")
yourini = ("Инициалы: ")

vibor = raw_input ("Начнем опрос? [y/n]: ")
print ('*' * 30)

while vibor == "y":
	usrname = raw_input ("Введи имя: ")
	usrfami = raw_input ("Ваша фамилия: ")
	usrage = raw_input ("Введи возраст: ")
	usrcity = raw_input ("Введи город: ")
	sps [1] = usrname
	sps [2] = usrfami
	sps [3] = usrage
	sps [4] = usrcity
	print ('*' * 30)
	print (yourname + sps [1])
	print (yourfamily + sps [2])
	print (yourage + sps [3])
	print (yourcity + sps [4])
	print (yourini + usrname[0] + usrfami[0])
	print ('*' * 30)

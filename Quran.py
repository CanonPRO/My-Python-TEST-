#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
@Author: Halid
@Date: 2015-6-3
# Тестовый скрипт
"""

print ('С именем Аллаха')
print ('-' * 20)
print (" ")

sura_1 = {1:'Во имя Аллаха, Милостивого, Милосердного!', 2:'Хвала Аллаху, Господу миров,', 3:'Милостивому, Милосердному,', 4:'Властелину Дня Воздаяния!', 5:'Тебе одному мы поклоняемся и Тебя одного молим о помощи.', 6:'Веди нас прямым путем,', 7:'путем тех, кого Ты облагодетельствовал, не тех, на кого пал гднев, и не заблудших.'}
sps_nu_sura = {1:'Сура 1 ', 2:'Сура 2 ', 3:'Сура 3 ', 4:'Сура 4 '}
sps_name_sura = {1:'Открывающая книгу', 2:'Корова', 3:'Семейство Имрана', 4:'Женщины'}
sps_ayat = {1:'1. ', 2:'2. ', 3:'3. ', 4:'4. ', 5:'5. ', 6:'6. ', 7:'7. ', 8:'8. '}

q = raw_input ("Введите номер суры: ")
print (" ")
print ('-' * 50)

if q == '1':
	print (sps_nu_sura[1] + sps_name_sura[1])
	print ('-' * 50)
	print (" ")
	otvet_1 = raw_input ("Прочитать всю суру? [y/n] Либо введите номер одного из 7-ми аятов: ")
	if otvet_1 == "y":
		print (" ")
		print ('-' * 50)
		print (sps_ayat[1] + sura_1[1])
		print (sps_ayat[2] + sura_1[2])
		print (sps_ayat[3] + sura_1[3])
		print (sps_ayat[4] + sura_1[4])
		print (sps_ayat[5] + sura_1[5])
		print (sps_ayat[6] + sura_1[6])
		print (sps_ayat[7] + sura_1[7])
		print ('-' * 50)
	elif otvet_1 == '1':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[1] + sura_1[1])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '2':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[2] + sura_1[2])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '3':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[3] + sura_1[3])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '4':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[4] + sura_1[4])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '5':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[5] + sura_1[5])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '6':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[6] + sura_1[6])
		print ('-' * 50)
		print (" ")
	elif otvet_1 == '7':
		print (" ")
		print ('-' * 50)
		print (sps_ayat[7] + sura_1[7])
		print ('-' * 50)
		print (" ")
		
elif q == 2:
	print (sps_nu_sura[2] + sps_name_sura[2])
	print (" ")

elif q == 3:
	print (sps_nu_sura[3] + sps_name_sura[3])
	print (" ")

elif q == 4:
	print (sps_nu_sura[4] + sps_name_sura[4])
	print (" ")
	

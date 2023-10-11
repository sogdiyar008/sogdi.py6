from math import* #помощь при случае необходимости

# Длина отрезка
# def distance(x1, y1, x2, y2):
#     return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
# print(distance((float(input('введите x1:'))), (float(input('введите y1:'))), (float(input('введите x2:'))), (float(input('введите y2:')))))

# Отрицательная степень
# def power(a, n):
#     res = 1
#     for i in range(abs(n)):
#         res *= a
#     if n >= 0:
#         return res
#     else:
#         return 1 / res
#
# print(power(float(input('введите А: ')), int(input('введите n: '))))

#  Числа Фибоначчи
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(int(input("номер числа Фиб.: "))))


# Високосный год
# Уже делали, поэтому я просто украду у себя же код свой:)
# def is_year_leap (year):
# 	if year % 400 == 0:
# 		print('TRUE')
# 	elif year%100==0:
# 		print('FALSE')
# 	elif year%4==0:
# 		print('TRUE')
# 	else:
# 		print('FALSE')
# while True:
# 	is_year_leap(int(input('введите год:  ')))

# квадрат
# def square (square):
# 	P=square*4
# 	S=square*square
# 	D=sqrt(square**2+square**2)
# 	return P, S, D
# print('1-периметр 2-площадь 3-диоганаль:  ',square(int(input('введи сторону квадрата: '))))


# сезоны
# def seasons(seas):
# 	seas=abs(seas%12)
# 	print(seas)
# 	if seas >= 9:
# 		return print('сейчас осень')
# 	elif seas >=6:
# 		return print('сейчас лето')
# 	elif seas >=3:
# 		return print('сейчас весна')
# 	elif seas ==0:
# 		return print('сейчас зима')
# 	elif seas > 0:
# 		return print('сейчас зима')
# seasons(int(input('введи номер месяца года: ')))

# БАНК
# a=int(input('вклад: '))
# year=int(input('через сколько лет?: '))
# for i in range(year):
# 	a=a+a/10
# print(round(a, 3))

# простые числа
# def is_prime(is_prime):
# 	assistant=0 #для того что бы помочь вывести один результат, а не повторные
#
# 	if is_prime>1:     #что бы определить является ли число проситым
# 		for i in range(2, is_prime):  #работает пока не найдет, простое ли число
# 			if is_prime % i==0:
# 				assistant =0
# 				break
# 			else:
# 				assistant=1
# 	else:
# 		assistant = 0
#
#
# 	if assistant == 0:
# 		print(f'число {is_prime} не является простым','\n')
# 	elif assistant == 1:
# 		print(f'число {is_prime} является простым','\n')
# while True:
# 	is_prime(int(input('проверка на простоты числа: ')))


# Правильная дата 
# def date(day, month, year):
# 	if day <= 0 or month <= 0 or year < 0:
# 		return False
# 	else:
# 		months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 		if year % 4 == 0:  months[1] = 29
# 		if day <= months[month - 1]:
# 			if month <= 12:
# 				return True
# 		return False
# print(date(int(input('день: ')), int(input('месяц: ')), int(input('год: '))))
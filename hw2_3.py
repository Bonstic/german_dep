'''
Требуется определить, является ли данный год високосным
(порядковый номер которых либо кратен 4, но при этом не кратен
100, либо кратен 400).
'''
year = int(input('Введите год'))
if (year%4 == 0 and year%100 !=0) or year%400 == 0:
    print('Высокосный')
else: print('Невысокосный')
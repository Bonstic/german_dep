'''
Напишите программу, в которой пользователь вводит три целых чиcла, а программа проверяет,
являются ли эти числа тремя последовательными элементами арифметической последовательности.
В арифметической последовательности каждый новый член получается прибавления к предыдущему определенного фиксированного числа.
'''

num_1 = int(input('Число 1:'))
num_2 = int(input('Число 2:'))
num_3 = int(input('Число 3:'))
if num_2 - num_1 == num_3 - num_2:
    print('Элементы арифм послед')
else: print('Не арифм послед')
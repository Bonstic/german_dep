'''
Напишите программу, в которой решается уравнение вида
А(А - 1)* x=sin(A) , причем при значении A = 0 должно вычисляться решение x= -1.
'''

import math
A = float(input('число А:'))
try:
    x = math.sin(A)/(A*(A-1))
    print(f'x={x}')
except:
    if A == 0:
        x = -1
        print(f'x={x}')
    else: print('Деление на ноль')

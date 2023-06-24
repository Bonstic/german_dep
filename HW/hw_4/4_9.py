#Создать матрицу, найти максимальное значение матрицы.

matrix = [[6,17,28],[9,14,37],[18,27,1]]
lst = []
for elem in matrix:
    lst.append(max(elem))
m_num = max(lst)
print(m_num)
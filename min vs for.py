'''
Встроенные функции min, max, sum и встроенный метод .count
в несколько раз быстрее for
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint
N = 10000
lst = [randint(0, N / 100) for i in range(N)]
# print(lst)
'''

TESTED_CODE = ''' 
# lst.count(100)

mn = 0
for i in range(N):
    if lst[i] == 100:
       mn += 1

# print(mn)
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1000))/5)


'''
min: for - 1.174, min - 0.312
max: for - 1.155, max - 0.308
sum: for - 2.135, sum - 0.202
.count: for - 0.918, .count - 0.176
'''

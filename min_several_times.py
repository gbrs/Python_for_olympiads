"""
если внутри цикла, мы обращаемся к min(lst)
интерпретатор честно каждый раз ищет min.
Надо один раз вне цикла его найти и использовать
"""


import timeit

NOT_REPITED_CODE = '''
from random import randint
N = 1000
lst = [randint(0, 100) for i in range(N)]
# print(lst)
'''

TESTED_CODE = ''' 

cnt = 0

for i in range(N):
    if lst[i] > min(lst) and lst[i] < max(lst):
       cnt += 1

# mn = min(lst)
# mx = max(lst)
# for i in range(N):
#     if lst[i] > mn and lst[i] < mx:
#        cnt += 1

# print(cnt)
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100))/5)


'''
lst[i] > min(lst) 1.779
mn = min(lst)     0.00974014
'''

'''
хм. reduce раза в полтора медленнее for. Хотя map - просто ураган
??? может это из-за того, что он импортируется?
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint
from functools import reduce

N = 500000
lst = [randint(0, N / 1000) for i in range(N)]
# print(lst)
sm = 0
'''

TESTED_CODE = ''' 
# for i in range(N):
#     sm += lst[i]

sm = reduce(lambda x, y: x + y, lst)
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1))/5)


'''
for: 0.0745
reduce: 0.108
'''

'''
list(map()) вдвое быстрее list comprehension.
Пайтон стайл list comprehension чуть лучше своего собрата
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint
N = 10000
lst = [randint(0, N / 1000) for i in range(N)]
# print(lst)
'''

TESTED_CODE = ''' 
lst = list(map(str, lst))
# lst = [str(lst[i]) for i in range(N)]
# lst = [str(i) for i in lst]
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100))/5)


'''
list comprehension: 0.322
list comprehension: 0.249
map: 0.0000288. Потому, что ничего и не делается (map - это итератор)?
если потом переводить map в список: 0.156
'''

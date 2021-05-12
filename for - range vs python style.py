'''
вау. Пайтон стайл таки всего раза в 1,5-2, но быстрее привычного range()
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint
N = 10000
lst = [randint(0, N / 1000) for i in range(N)]
# print(lst)
sm = 0
'''

TESTED_CODE = ''' 
# for i in range(N):
#     sm += lst[i]

for number in lst:
    sm += number
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100))/5)


'''
python style: 0.113
range: 0.194
'''

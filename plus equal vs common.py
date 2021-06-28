'''
моно...уально
'''


import timeit

NOT_REPITED_CODE = '''
sm = 0
'''

TESTED_CODE = '''
for i in range(10000):
    sm = sm + 1000
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1000))/5)


'''
+=  : 1.335
= _+_: 1.324
'''

'''
Непонятно. На маленьких строчках конкатенация выигрывает в разы.
Но join на порядки лучше, когда к строке надо присоединять строки длиннее ~1000 знаков
'''

import timeit

NOT_REPITED_CODE = '''
s = 'a' * 5000
a = 'a' * 5000
'''

TESTED_CODE = '''
s = s + a
'''

# s = s + a  # 0.23 2.81
# s += a  # 0.22 2.72
# ''.join([s, a])  # 0.46 0.00133! (5000знаков+5000знаков)

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1000))/5)

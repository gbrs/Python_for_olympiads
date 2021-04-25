'''
list comprehension вдвое быстрее for?
'''

import timeit

NOT_REPITED_CODE = '''

'''

TESTED_CODE = '''
lst = []
for i in range(1000000):
    lst.append(i)
# lst = [i for i in range(1000000)]
'''

# вывод на печать результатов 5 (по умолчанию) измерений number = 100 повторов
print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100)) / 5)

# 1.876
# lst = []
# for i in range(100000):
#     lst.append(i)

# lst = [i for i in range(100000)]  # 0.959

'''
питонячий O(N) все равно быстрее вероятно сишного O(N*logN),
вшитого в сортировки Питона
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint
N = 1000000
lst = [randint(0, N) for i in range(N)]
# print(lst)
mx1 = mx2 = -1
'''

TESTED_CODE = '''
# for number in lst:
#     if number >= mx1:
#         mx2 = mx1
#         mx1 = number
#     elif number >= mx2:
#         mx2 = number

sorted(lst)[-2]

# lst.sort()
# lst[-2]
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1))/5)


'''
for - 0.0937
sorted - 0.658
sort - 0.631
'''

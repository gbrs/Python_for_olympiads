'''
map - просто ураган по сравнению с for. Почему!? Так не д.б.
'In addition, the list comprehension executes much faster
than the solution using map and lambda. This is because calling a lambda function
creates a new stack frame while the expression in the list comprehension
is evaluated without creating a new stack frame' /ван Россум/.
Поскольку читабельность важна, то часто лист компрехеншн лучше. Он - более питонячий,
посему он рекомендуется создателями Питона.
map занимает меньше места - хорош когда нам не нужны все значения сразу.
Гвидо ван Россум называет map ошибкой
и призывает использовать вместо него включения (компрехеншин?)
'''


import timeit

NOT_REPITED_CODE = '''
from random import randint

N = 100000
lst1 = [randint(0, N // (N // 10)) for i in range(N)]
# print(lst)
'''

TESTED_CODE = ''' 
lst = lst1

# for i in range(N):
#     lst[i] = lst[i]**2

# for i in lst:
#     i = i**2

# lst = [i**2 for i in lst]

lst = map(lambda x: x**2, lst)
'''

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100))/5)


'''
for i in range: 0.100
for i in lst: 0.0798
list comprehension: 0.0749
map: 0.00000648
'''

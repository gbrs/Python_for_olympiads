'''
' '.join(map(str, lst)) быстрее *lst.
С увеличением длины списка преимущество возрастает?
Время выполнения join иногда различалось на порядок,
перезагрузка пайчарма не помогала. Что-то делаю не так?
'''



import timeit

NOT_REPITED_CODE = '''
lst = [0] * 10000
'''

TESTED_CODE = '''
print(' '.join(map(str, lst)))
'''

# вывод на печать результатов 5 (по умолчанию) измерений number = 100 повторов
print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100)) / 5)

# print(*lst) 12.4
# print(' '.join(map(str, lst))) 0.897

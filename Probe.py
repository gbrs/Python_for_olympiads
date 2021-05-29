import timeit

NOT_REPITED_CODE = '''

'''

TESTED_CODE = '''

'''

# вывод на печать результатов 5 (по умолчанию) измерений number = 100 повторов
print(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=100))

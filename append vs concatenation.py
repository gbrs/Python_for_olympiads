'''
не увидел разницы в скорости между append/extend и конкатенацией
'''

import timeit

NOT_REPITED_CODE = '''
lst = [0] * 1000
lst2 = [1] * 10000
'''

TESTED_CODE = '''
# lst.extend(lst2)
lst += lst2
'''

# lst.append(1)  # 0.0119
# lst += [1]  # 0.0144

# lst.extend(lst2)  # 0.897
# lst += lst2  # 0.917

print(sum(timeit.repeat(stmt=TESTED_CODE, setup=NOT_REPITED_CODE, number=1000))/5)


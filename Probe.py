from random import randint
N = 10000
lst = [randint(0, N / 1000) for i in range(N)]
sm = 0

# for i in range(N):
#     sm += lst[i]

for number in lst:
    sm += number

print(sm)


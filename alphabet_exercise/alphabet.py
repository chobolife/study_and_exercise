import random

result_number = 10
str_b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_s = 'abcdefghijklmnopqrstuvwxyz'

result = []
for i in range(len(str_b)):
    result.append(str_s[i] + str_b[i])

with open('result.txt', 'w') as f:
    for i in range(result_number):
        random.shuffle(result)
        f.write("{0}\n".format(' , '.join(result)))


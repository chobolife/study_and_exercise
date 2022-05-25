import random

result_number = 10
result_problem = 36

list_ones = []
for i in range(10):
    for j in range(10-i, 10):
        list_ones.append([i,j])

list_tens = []
for i in range(1, 10):
    for j in range(1, 10-i):
        list_tens.append([i,j])

for i in range(result_number):
    if result_number > 10:
        fname = "result_{0:02}.txt".format(i)
    else:
        fname = "result_{0}.txt".format(i)
    with open(fname, 'w') as f:
        for j in range(result_problem):
            choice_one = random.choice(list_ones)
            choice_ten = random.choice(list_tens)
            f.write('{0}{1}+{2}{3}=\n'.format(choice_ten[0], choice_one[0], choice_ten[1], choice_one[1]))
            if j == 17:
                f.write('\n')

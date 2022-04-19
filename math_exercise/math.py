import random

result_number = 10
source_file_list = [
        'list_goal1.txt',
        'list_goal2.txt',
        'list_goal3.txt',
        'list_goal4.txt',
        'list_goal7.txt',

        'list_goal5.txt',

#        'list_goal6.txt',
#        'list_goal8.txt',
#        'list_goal9.txt',
        ]

result = []
for source_file in source_file_list:
    with open(source_file, 'r') as f:
        result += f.readlines()

print(result)

print("total lines: {0}".format(len(result)))

for i in range(result_number):
    random.shuffle(result)
    if result_number > 10:
        fname = "result_{0:02}.txt".format(i)
    else:
        fname = "result_{0}.txt".format(i)
    with open(fname, 'w') as f:
        j = 0
        for line in result:
            j = j + 1
            f.write(line)
            if j == 8:
                j = 0
                f.write('\n')


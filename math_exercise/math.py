import random

result_number = 2
source_file_list = [
#        'list_goal1.txt',
#        'list_goal2.txt',
#        'list_goal3.txt',
#        'list_goal4.txt',
#        'list_goal7.txt',

#        'list_goal5.txt',

#        'list_goal6.txt',
#        'list_goal8.txt',
#        'list_goal9.txt',

        'list_plus_18.txt',   #  1
        'list_plus_17.txt',   #  2
        'list_plus_16.txt',   #  3
        'list_plus_15.txt',   #  4
        'list_plus_14.txt',   #  5
        'list_plus_13.txt',   #  6
        'list_plus_12.txt',   #  7
        'list_plus_11.txt',   #  8
        'list_plus_10.txt',   #  9
        'list_plus_9.txt',    # 36
        ]

num = 0
read_file = []
result = []
for source_file in source_file_list:
    with open(source_file, 'r') as f:
        read_file = f.readlines()
        if num + len(read_file) > 45:
            random.shuffle(read_file)
            read_file = read_file[:45-num]
        result += read_file
        num += len(read_file)

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
            if j == 15:
                j = 0
                f.write('\n')


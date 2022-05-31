import random
import configparser
import list_print

cfg = configparser.ConfigParser()
cfg.read("./env.ini")
result_file   = cfg.getint('option', 'result_file')
result_chunk  = cfg.getint('option', 'result_chunk')
result_repeat = cfg.getint('option', 'result_repeat')

list_ones = []
for i in range(10):
    for j in range(1, i+1):
        list_ones.append([i,j])

list_tens = []
for i in range(1, 10):
    list_tens.append(i)

for i in range(result_file):
    fname = "result_{0}.txt".format(i)
    with open(fname, 'w') as f:
        for repeat in range(result_repeat):
            result = []
            for j in range(result_chunk):
                choice_one = random.choice(list_ones)
                choice_ten = random.choice(list_tens)
                result.append([choice_ten*10+choice_one[0], choice_one[1]])
            list_print.list_print(f, result_chunk, 0, result)

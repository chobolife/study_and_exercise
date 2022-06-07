import random
import configparser
import list_print

cfg = configparser.ConfigParser()
cfg.read("./env.ini")
result_file   = cfg.getint('option', 'result_file')
result_chunk  = cfg.getint('option', 'result_chunk')
result_repeat = cfg.getint('option', 'result_repeat')

for i in range(result_file):
    fname = "result_{0}.txt".format(i)
    with open(fname, 'w') as f:
        for repeat in range(result_repeat):
            result = []

            for j in range(result_chunk):
                sign = random.randint(0, 1)
                if sign == 1:
                    no1 = random.randint(20, 98)
                    no2 = random.randint(1, 99-no1)
                else:
                    no1 = random.randint(20, 99)
                    no2 = random.randint(10, no1-10)

                result.append([no1, no2, sign])

            list_print.list_print_with_sign(f, result_chunk, result)

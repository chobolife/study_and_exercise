def list_print(f, chunk, sign, result):
    if sign == 1:
        s_sign = '+'
    else:
        s_sign = '-'

    for j in range(chunk):
        f.write('\t\t\t{0}'.format(result[j][0]))
    f.write('\n')
    for j in range(chunk):
        f.write('\t\t{0}\t{1}'.format(s_sign, result[j][1]))
    f.write('\n\n\n')


def list_print_with_sign(f, chunk, result):
    for j in range(chunk):
        f.write('\t\t\t{0}'.format(result[j][0]))
    f.write('\n')
    for j in range(chunk):
        if result[j][2] == 1:
            s_sign = '+'
        else:
            s_sign = '-'
        f.write('\t\t{0}\t{1}'.format(s_sign, result[j][1]))
    f.write('\n\n\n')

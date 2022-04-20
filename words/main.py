def read_data(filename):
    result = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            s = line[:-1].split('	')
            for item in s:
                result.append(item)
    return result

def write_result(list_out, filename):
    with open(filename, "w") as f:
        for item in list_out:
            f.write("{}\n".format(item))

list_in = read_data("word_7A.txt")

set_result = set()
for word in list_in:
    set_result.add(word)

list_result = list(set_result)
list_result.sort()

write_result(list_result, "result_word_7A.txt")

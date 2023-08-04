file_path = 'E:\\Programming\\AutoCalculator\\math.txt'


def read_file(file_path):
    file = open(file_path)
    return file


def split_file_in_line(file_no_in_line):
    text = file_no_in_line.read()
    text_in_line = text.split("\n")
    return text_in_line


def function_split(file_need_split):
    file_rename = (file_need_split.replace(' ', ';'))
    file_split = file_rename.split(';')
    return file_split


def math(file_str):
    for line_str in file_str:
        example_str = line_str[3::]
        example_int = function_split(example_str)
        first_num = int(example_int[0])
        two_num = int(example_int[2])
        if example_int[1] == '+':
            result = first_num + two_num
        elif example_int[1] == '-':
            result = first_num - two_num
        elif example_int[1] == '/':
            result = first_num / two_num
        elif example_int[1] == '*':
            result = first_num * two_num

        print(result)



math(split_file_in_line(read_file(file_path)))
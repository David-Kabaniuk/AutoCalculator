file_path = 'E:\\Programming\\AutoCalculator\\math.txt'


def read_file(file_path):
    file = open(file_path)
    return file


def split_file_in_line(file_no_in_line):
    text = file_no_in_line.read()
    text_in_line = text.split("\n")
    return text_in_line


def math(file_int):
    for example in file_int:
        print(example)


math(split_file_in_line(read_file(file_path)))
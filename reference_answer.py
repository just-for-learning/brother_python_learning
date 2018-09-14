def print_odd_even():
    """
    question 1
    :return: None
    """
    print("50以内的奇数和偶数如下：")
    odd_number = []
    even_number = []
    for number in range(51):
        if number == 0:
            print("0 既不是奇数也不是偶数")
        elif number % 2 == 0:
            even_number.append(number)
        else:
            odd_number.append(number)
    print("奇数: ")
    print(odd_number)
    print("偶数: ")
    print(even_number)


def print_multi_table():
    """
    question 2
    :return: None
    """
    for i in range(1, 22):
        line = str(i) + " : "
        for j in range(1, i + 1):
            line += str(j) + " x " + str(i) + " = " + str(i * j) + ", "
        print(line.rstrip(", "))


def print_file():
    """
    question 3
    :return: None
    """
    with open("./print_file.txt", 'r', encoding='utf8') as f:
        file = f.read()
        print(file)


def copy_file():
    """
    question 4
    :return: None
    """
    with open("./print_file.txt", 'r', encoding='utf8') as f:
        with open("./print_file_copy.txt", 'w', encoding='utf8') as f_copy:
            f_copy.write(f.read())
    print("文件复制已完成")


if __name__ == '__main__':
    """
    there are 4 function as below, you can excite it by uncomment the line.
    """
    # print_odd_even()
    # print_multi_table()
    # print_file()
    # copy_file()
    pass

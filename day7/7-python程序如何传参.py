

import sys


# print(type(sys.argv))
# print(sys.argv)

def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf8')
    file.write('你在干什么！')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])

# 作者: 王道 龙哥
# 2024年12月31日10时42分53秒
# xxx@qq.com


def open_r():
    """
    读取文件
    :return:
    """
    file = open('file2.txt', mode='r', encoding='utf-8')
    text = file.read()  # 读出来都是字符串
    print(text)
    file.close()


def open_rw():
    """
    读取文件,写文件
    :return:
    """
    file = open('file2.txt', mode='r+', encoding='utf-8')
    text = file.read()  # 读出来都是字符串
    print(text)
    file.write('world')  # 写到末尾了
    file.close()


def open_w():
    """
    练习w模式
    :return:
    """
    file = open('file3', mode='w', encoding='utf-8')  # 文件不存在就会创建，存在就会清空
    # file.write('hello坚持学习')
    file.close()


def open_a():
    """
    练习a模式，每次写的时候写到文件末尾
    :return:
    """
    file = open('file1', mode='a', encoding='utf-8')
    file.write('how')  # 使用r+模式，打开后在开头，内容直接覆盖
    file.close()


def use_readline():
    # 打开文件
    file = open("file2.txt", mode='r', encoding='utf8')

    while True:
        # 读取一行内容
        text = file.readline()

        # 判断是否读到内容,读取到文件末尾拿到的是一个空字符串
        if not text:
            break
            text = file.readline()
    # 每读取一行的末尾已经有了一个 `\n`
        print(text, end='')
    # 关闭文件
    file.close()


if __name__ == '__main__':
    # open_r()
    # open_rw()
    # open_w()
    # open_a()
    use_readline()

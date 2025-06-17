

import os


def use_rename():
    """
    理解相对路径，绝对路径
    :return:
    """
    # os.rename('dir2/file3', 'dir2/file1')
    os.remove('dir2/12')  # remove只能删除文件不能删除文件夹
    os.remove('dir2/file2')


def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    # os.mkdir('dir2')
    # os.rmdir('dir1')
    print(os.getcwd())
    os.chdir('dir2')
    file = open('file1', 'r+', encoding='utf8')
    file.write('hello world,nice to meet you!')
    file.seek(0, 0)
    test = file.readline(11)
    # test = file.read()
    print(test)
    file.close()


def change_dir():
    """
    改变路径
    :return:
    """
    print(os.getcwd())  # 打印当前路径
    os.chdir('dir2')    # 类似于进入这个目录  进入到dir2目录下
    print(os.getcwd())  # 打印当前路径


def scan_dir(current_path, width):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            scan_dir(new_path, width + 4)


def use_stat(file_path):
    """
    文件大小
    :param file_path:
    :return:
    """
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size, file_info.st_uid,
                                                 file_info.st_mode, file_info.st_mtime))
    #  用format函数把文件信息打印出来,这个只是以后面的形式把他打印出来！
    #  uid0表示文件所有者（顶级用户），mode表示文件权限，mtime表示文件最后修改时间
    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    # 把秒数转为字符串时间
    print(strftime("%Y-%m-%d %H:%M:%S", gm_time))


if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # change_dir()
    # scan_dir('.', 0)
    use_stat('file10')  # 显示的时间是文件file10的创建时间！

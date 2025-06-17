class Women:
    """
    私有属性和私有方法只能在类内部访问
    """

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __secret(self):
        print(f'{self.name} 年龄{self.__age}')

    def boy_friend(self):
        self.__secret()


if __name__ == '__main__':
    xiaohong = Women('小红', 18)
    xiaohong.boy_friend()
    # print(xiaohong._Women__age)  不这么写

# 作者: 王道 龙哥
# 2024年12月30日14时21分23秒
# xxx@qq.com
# 作者: 王道 龙哥
# 2024年12月30日14时08分52秒
# xxx@qq.com

class Parent:
    def __init__(self, height):
        self.height = height


class Son1(Parent):
    def __init__(self, age, *args):
        self.age = age
        super().__init__(*args)


class Son2(Parent):
    def __init__(self, score, *args):
        self.score = score
        super().__init__(*args)


class Grandson(Son1, Son2):
    def __init__(self, name, *args):
        self.name = name
        # super().__init__(*args)


if __name__ == '__main__':
    xiaoming = Grandson('小明', 18, 98.5, 175)  # 姓名，年龄，分数,身高
    # print(xiaoming.name)
    # print(xiaoming.age)
    # print(xiaoming.score)
    # print(xiaoming.height)
    print(Grandson.__mro__)

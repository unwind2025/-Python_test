# 作者: 王道 龙哥
# 2024年12月31日09时15分18秒
# xxx@qq.com

class A:
    def __init__(self):  # 父类私有属性
        self.__age = 18

    def base_age(self):  # 父类私有属性
        print(self.__age)

class B(A):
    # def __init__(self):
    #     super().__init__()
    def get_age(self):
        self.base_age()  # 调用父类方法


if __name__ == '__main__':
    zhangsan = B()  # 实例化子类对象
    zhangsan.get_age()  # 调用父类方法

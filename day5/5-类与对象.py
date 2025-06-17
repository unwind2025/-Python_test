# 作者: 王道 龙哥
# 2024年12月28日10时58分15秒
# xxx@qq.com

# 类里边的叫方法
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(self.name + '正在奔跑')

    def eat(self):
        print(self.name + '正在吃东西')


# 实例化
elephant = Person('大象', 18, 1.75)
print(elephant.name, elephant.age, elephant.height)
elephant.run()
tiger = Person('老虎', 17, 1.65)
print(tiger.name, tiger.age, tiger.height)
tiger.run()

print('-'*50)
print(dir(Person))
print('-'*50)
print(dir(elephant))
print('-'*50)
elephant.name = '大黄蜂'

# 作者: 王道 龙哥
# 2024年12月31日09时46分11秒
# xxx@qq.com
from module1 import test1
from module2 import test1 as module2_test1
import random

# import test1
# from module1 import test1 as module1_test1  # as 给test1起别名
# 这样导入的类名和方法名会冲突，因此需要给类名和方法名加上模块名作为前缀

test1()
module2_test1()

print(random.__file__)  # 查看模块所在路径
rand = random.randint(1, 100)
print(rand)



# 容器是空就是假，不可以去用==False去对应
if []:
    print("非空列表")
else:
    print("空列表")

if {}:
    print("非空字典")
else:
    print("空字典")

# 空的容器和None是不相等的

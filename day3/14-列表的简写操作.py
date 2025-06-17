
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(f'数据{a},地址{id(a)}')
print(a * 2)
a += b  # 等价于a.extend(b)
print(f'操作后，数据{a},地址{id(a)}')

print(a[2:6])

x = int(input())
a = 1
b = 1
for i in range(100000):
    new = a + b
    a = b
    b = new
    if x == 1:
        print('Число принадлежит к числам Фибоначчи')
        break
    if x == new:
        print('Число принадлежит к числам Фибоначчи')
        break
    if i == 99999:
        print('Число не принадлежит к числам Фибоначчи')
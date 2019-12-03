import matplotlib.pyplot as plt
import math
f1 = [] # список значений х
f2 = [] # список значений y

try:
    a = int(input('введите значение a:'))
    x = int(input('введите начальное значение x:'))
    xn = int(input('введите конечное значение x:'))
    k = int(input('введите шаг вычисления функции k:'))
except ValueError:
    print('введено некорректное значение')
    exit(1)

z = int(input('введите номер примера(1, 2, 3):'))
if z == 1:
    for i in range(x, xn + 1, k):
        if (21*a**2+a*i-36*i**2) == 0:
            print('значение функции невозможно посчитать в точке х=', i, 'т.к. при таком значениии знаменатель равен 0')
        else:
            G = -(2*(7*a**2-17*a*i+6*i**2))/(21*a**2+a*i-36*i**2)
            f1.append(i)
            f2.append(G)
    plt.plot(f1,f2)
    plt.show()

elif z == 2:
    for i in range(x, xn + 1, k):
        if (math.pi*(-8*a**2+6*a*i+9*i**2)) == 0:
            print('значение функции невозможно посчитать в точке х=', i, 'т.к. при таком значениии знаменатель равен 0')
        else:
            F = (math.sin(math.pi*(-8*a**2+6*a*i+9*i**2)))/(math.pi*(-8*a**2+6*a*i+9*i**2))
            f1.append(i)
            f2.append(F)
    plt.plot(f1,f2)
    plt.show()

elif z == 3:
    for i in range(x, xn + 1, k):
        if 8*a**2-27*a*i-20*i**2 == 0:
            print('значение функции невозможно посчитать в точке х=', i, 'т.к. при таком значениии тангенс равен 0')
        else:
            Y = -math.atan(8*a**2-27*a*i-20*i**2)
            f1.append(i)
            f2.append(Y)
    plt.plot(f1,f2)
    plt.show()

else:
    print('такого примера несуществует')
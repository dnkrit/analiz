import matplotlib.pyplot as plt

x = [2, 6, 8, 14, 20]
y = [6, 4, 10, 12, 16]

plt.plot(x, y)
#название графика
plt.title("Пример простого линейного графика")
#название осей
plt.xlabel ("Подпись для оси X")
plt.ylabel ("Подпись для оси Y")

plt.show()

import matplotlib.pyplot as plt

data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 6]

plt.hist(data, bins=6)
#bins - \то кол-во интервалов

plt.xlabel ("Подпись для оси X")
plt.ylabel ("Подпись для оси Y")
plt.title("Пример гистограммы")

plt.show()

import matplotlib.pyplot as plt

data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]

plt.hist(data, bins=6)
#bins - \то кол-во интервалов

plt.xlabel ("часы сна X")
plt.ylabel ("кол-во людей Y")
plt.title("Гистограммы часов сна")

plt.show()

import matplotlib.pyplot as plt

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.xlabel ("Ось X")
plt.ylabel ("Ось Y")
plt.title("Диаграмма рассеивания")

plt.show()


import numpy as np

a = np.array([1, 2, 3, 4])
#Можно сделать масив из списка. Отличие массива и списка в том, что массив - это однотипные данные

print(a)


import numpy as np

a = np.zeros((3, 3,))
#Числа обозначают размер массива

print(a)


import numpy as np

a = np.ones((2, 5))
#Числа обозначают размер массива
#2 списка по 5 элементов

print(a)


import numpy as np

a = np.random.random((4, 5))
#Выводится 4 строки по 5 элементов (рандомные значения)
#Рандомные значения выводятся от 0 до 1
print(a)


import numpy as np

a = np.arange(0, 10, 2)
#В значениях указывается начало, конец и шаг
print(a)


import numpy as np

a = np.linspace(start=0, stop=13, num=10)
#Указываем начало и конец, и сколько чисел должно поулчится. Равнораспределенные от 0 до 13
print(a)



import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=-10, stop=10, num=100)

y = x**2
#plt - это функция для построения графика
plt.plot (x, y)
plt.xlabel ("Ось X")
plt.ylabel ("Ось Y")
plt.title ("График функции y = x**2")
plt.grid(True)
plt.show()




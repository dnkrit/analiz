import numpy as np
import matplotlib.pyplot as plt

# Генерация двух массивов из 100 случайных чисел от 0 до 1
x = np.random.rand(100)
y = np.random.rand(100)

# Построение диаграммы рассеяния
plt.scatter(x, y)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

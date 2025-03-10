import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0         # Среднее значение
std_dev = 1      # Стандартное отклонение
num_samples = 1000  # Количество случайных чисел

# Генерация данных с нормальным распределением
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)  # массив из 50 случайных чисел для оси X
y = np.random.rand(50)  # массив из 50 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Отображение графика
plt.show()
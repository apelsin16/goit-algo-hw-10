import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла методом Монте-Карло
N = 100000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = f(x_random)
monte_carlo_integral = (b - a) * np.mean(y_random)

# Перевірка з використанням функції quad
quad_integral, quad_error = spi.quad(f, a, b)

# Побудова графіка функції та інтегралу
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Виведення результатів
print("Інтеграл методом Монте-Карло: ", monte_carlo_integral)
print("Інтеграл за допомогою quad: ", quad_integral)
print("Абсолютна похибка методу Монте-Карло: ", abs(monte_carlo_integral - quad_integral))

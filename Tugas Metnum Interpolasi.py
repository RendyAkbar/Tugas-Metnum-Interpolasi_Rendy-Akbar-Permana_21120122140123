import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import lagrange
from scipy.interpolate import BarycentricInterpolator

tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])

polinomial_lagrange = lagrange(tegangan, waktu_patah)
polinomial_newton = BarycentricInterpolator(tegangan, waktu_patah)

y_lagrange = polinomial_lagrange(x_range)
y_newton = polinomial_newton(x_range)

x_range = np.linspace(5, 40, 400)

plt.figure(figsize=(10, 6))
plt.plot(tegangan, waktu_patah, 'o', label='Titik Data', markersize=8) 
plt.plot(x_range, y_lagrange, color='yellow', label='Interpolasi Lagrange')
plt.plot(x_range, y_newton, '--',	color='Red',	label='Interpolasi Newton')
plt.xlabel('Tegangan') 
plt.ylabel('Waktu Patah')
plt.title('Interpolasi Polinomial Lagrange dan Interpolasi Polinomial Newton') 
plt.legend()
plt.grid(True)
plt.show()


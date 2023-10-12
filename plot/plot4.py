import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 100)  # zakres od -4 do 4, 100 punktów
y = x**2

plt.plot(x, y)
plt.show()

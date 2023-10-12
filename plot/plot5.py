import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 10000)
print(x)
y = np.sin(x)

plt.plot(x, y)
plt.savefig("sinus.png")
plt.show()

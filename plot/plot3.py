import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(1, 100):
    x.append(i)
    y.append(math.pow(1 + 1 / i, i))


plt.plot(x, y)

plt.show()

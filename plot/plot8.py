# http://mfranczak.pl/smok-heighwaya/

import matplotlib.pyplot as plt
import random as rnd

x = [0]
y = [0]

for i in range(1, 10000):
    los = rnd.random()
    if los < 0.5:
        x.append(-0.4 * x[i - 1] - 1)
        y.append(-0.4 * y[i - 1] + 0.1)
    else:
        x.append(0.76 * x[i - 1] - 0.4 * y[i - 1])
        y.append(0.4 * x[i - 1] + 0.76 * y[i - 1])

plt.plot(x, y, ".")
plt.show()

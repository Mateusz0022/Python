import matplotlib.pyplot as plt

x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
y = [16, 9, 4, 1, 0, 1, 4, 9, 16]

plt.plot(x, y, "rx")
plt.title("Przykładowy wykres")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.show()

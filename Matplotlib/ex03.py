import matplotlib.pyplot as plt

x = range(-100, 110, 10)
y = []

for i in x:
    y.append(-i**2)

plt.plot(x, y)

plt.axhline(0, linewidth=6)
plt.axhline(-2000, linewidth=6)
plt.axvline(-75, linewidth=6)
plt.axvline(75, linewidth=6)

plt.xlabel("x")
plt.ylabel("y")

plt.xlim(-76, 76)
plt.ylim(-2000, 0)

plt.show()
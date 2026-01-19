import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 5)
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Line Plot")
plt.savefig("line.png")
plt.close()

plt.bar(["A", "B", "C"], [5, 7, 3])
plt.title("Bar Chart")
plt.savefig("bar.png")
plt.close()
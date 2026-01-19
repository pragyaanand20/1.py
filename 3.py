import numpy as np

a = np.array([1, 2, 3, 4])
b = np.arange(0, 10, 2)
c = np.linspace(0, 1, 5)

d = np.arange(6).reshape(2, 3)

print("Array:", a)
print("Arange:", b)
print("Linspace:", c)
print("Reshaped:\n", d)

print("Square root:", np.sqrt(a))
print("Mean:", np.mean(a))

np.random.seed(0)
print("Random:", np.random.rand(3))
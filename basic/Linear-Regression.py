import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5], dtype=np.float32)
y = np.array([1, 3.0, 2, 3, 5], dtype=np.float32)

plt.scatter(x, y)


x_mean = np.mean(x)
y_mean = np.mean(y)

num=0.0
d= 0.0

for i in range(len(x)):
    num += (x[i] - x_mean) * (y[i] - y_mean)
    d += (x[i] - x_mean) ** 2
    a=num/d
    b=y_mean - a * x_mean
y_hat = a * x + b

plt.figure(2)
plt.scatter(x, y)

plt.plot(x, y_hat, color='r')

x_predict = 4.8
y_predict = a * x_predict + b

plt.scatter(x_predict, y_predict, color='g', marker='x')


plt.show()
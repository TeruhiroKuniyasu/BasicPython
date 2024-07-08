import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

# 観測値 x: 初項0，末項5，項数100の等差数列
x = np.linspace(0, 5, 100)

# ノイズ noise: 標準正規分布に従う100個の乱数
noise = np.random.randn(100)

# 目標値 t を定義
def y(x):
    return 3 - 5 * x + x**2

t = y(x) + noise

# プロット
plt.scatter(x, t)
plt.xlabel('x')
plt.ylabel('t')
plt.title('Scatter plot of x vs t')
plt.show()

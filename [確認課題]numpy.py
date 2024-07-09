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

x0 = np.ones_like(x)
x1 = x
x2 = x**2

X = np.vstack((x0, x1, x2)).T

# 回帰係数を計算
w = np.linalg.inv(X.T @ X) @ X.T @ t
w0, w1, w2 = w

# 予測値を計算
pred_y = w0 + w1 * x + w2 * x ** 2

# プロット
plt.scatter(x, t)
plt.plot(x, pred_y, linewidth=2, color="red", label="Pred")
plt.plot(x, y(x), linewidth=2, color="green", label="True")
plt.legend()
plt.xlabel('x')
plt.ylabel('t')
plt.title('Scatter plot with true and predicted lines')
plt.show()

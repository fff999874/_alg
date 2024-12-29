import numpy as np

def riemann_sum(f, a, b, n):
    """
    計算一維函數 f 在區間 [a, b] 上的黎曼和

    參數:
        f: 被積函數
        a: 積分下限
        b: 積分上限
        n: 分割數

    回傳:
        黎曼和
    """
    dx = (b - a) / n
    x = np.linspace(a + dx/2, b - dx/2, n)
    return np.sum(f(x)) * dx

def monte_carlo(f, a, b, N):
    """
    計算一維函數 f 在區間 [a, b] 上的蒙地卡羅積分

    參數:
        f: 被積函數
        a: 積分下限
        b: 積分上限
        N: 取樣點數

    回傳:
        蒙地卡羅積分
    """
    x = np.random.uniform(a, b, N)
    y = np.random.uniform(a, b, N)
    z = np.random.uniform(a, b, N)
    return np.mean(f(x, y, z)) * (b-a)**3

# 定義被積函數
def f(x, y, z):
    return 3*x**2 + y**2 + 2*z**2

# 積分區域
a, b = 0, 1

# 分割數 (黎曼積分)
n = 100

# 取樣點數 (蒙地卡羅積分)
N = 1000000

# 計算三重積分
result_riemann = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            x = a + i/n
            y = a + j/n
            z = a + k/n
            result_riemann += f(x, y, z) / n**3

result_monte_carlo = monte_carlo(f, a, b, N)

print("黎曼積分結果:", result_riemann)
print("蒙地卡羅積分結果:", result_monte_carlo)

## 參考 gemini
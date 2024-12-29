# 用遞迴+查表

def power2n_d(n, a=None):
    # 初始化查表
    if a is None:
        a = {}
    
    # 如果結果已經在查表中，直接返回
    if n in a:
        return a[n]
    
    # 基本情況
    if n == 0:
        return 1

    # 遞迴計算並存入查表
    a[n] = 2 * power2n_d(n - 1, a)
    return a[n]

# 測試
print('power2n_d(10) =', power2n_d(10))

# 參考老師教材和gpt
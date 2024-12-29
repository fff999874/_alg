def my_permutation(elements):
    """
    計算給定元素的所有排列組合
    :param elements: 一個列表，包含要排列的元素
    :return: 包含所有排列的列表
    """
    if len(elements) == 0:
        return [[]]  # 空列表的排列只有一種：空排列

    permutations = []
    for i in range(len(elements)):
        # 固定當前元素，對剩下的元素遞迴進行排列
        current = elements[i]
        remaining = elements[:i] + elements[i+1:]
        for perm in my_permutation(remaining):
            permutations.append([current] + perm)

    return permutations

# 測試程式
if __name__ == "__main__":
    elements = [1, 2, 3]
    print("Input:", elements)
    print("Permutations:", my_permutation(elements))

# 參考 gemini
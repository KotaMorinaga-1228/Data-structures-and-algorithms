# -*- coding: utf-8 -*-

def knapsack(item, C):
    # TODO: DP表の作成までのプログラムを完成せよ
    n = len(item)
    G = [[0 for j in range(C+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, C+1):
            if item[i-1][1] > j:
                G[i][j] = G[i-1][j]
            else:
                G[i][j] = max(G[i-1][j], G[i-1][j-item[i-1][1]] + item[i-1][0])

    # DP 表から選んだ品物を探索
    selected = []   # 解に含まれる品物リスト
    j = C           # DP 表の列を示すインデックス
    for i in range(n, 0, -1):
        if j <= 0:
            break
        elif G[i-1][j] == G[i][j]:
            continue
        else:
            selected.append(item[i-1])
            j = j - item[i-1][1]
    return selected


if __name__ == '__main__':
    # 品物リスト（価値， 重量）
    item = [(280, 3), (350, 4), (620, 2), (120, 1)]
    print("品物リスト：", item)

    # 最適解を探索
    C = 6  # 重量の上限
    selected = knapsack(item, C)

    # 最適解を表示
    print("最適解：", selected)

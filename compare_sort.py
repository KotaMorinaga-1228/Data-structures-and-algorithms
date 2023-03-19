# -*- coding: utf-8 -*-
import time
import random

from bubble import bubble_sort
from quick import quick_sort
from merge import merge_sort

# 乱数のシードを固定
random.seed(1)

if __name__=="__main__":
    # ランダム配列を生成
    N = 10000 # データ数
    MAX = 10000000 # 最大値
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測
    s = time.time()
    bubble_sort(A) # バブルソート
    exec_time = time.time() - s
    print("バブルソート 実行時間：", exec_time)

    # ランダム配列を生成
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測
    s = time.time()
    quick_sort(A, 0, N-1) # クイックソート
    exec_time = time.time() - s
    print("クイックソート 実行時間：", exec_time)

    # ランダム配列を生成
    A = []
    for i in range(N):
        A.append(random.randint(0, MAX))
    # 実行時間計測
    s = time.time()
    merge_sort(A, 0, N-1) # マージソート
    exec_time = time.time() - s
    print("マージソート 実行時間：", exec_time)
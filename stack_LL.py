#!/usr/bin/env python
# coding: utf-8

# In[3]:


# -*- coding: utf-8 -*-

# 連結リストの各セル
class Cell:
    def __init__(self, val):
        self.val = val      # 要素が持つ値
        self.next = None    # 次のセルへのポインタ

# スタック
class Stack:
    def __init__(self):
        self.top = None

    # スタック配列内部を表示する関数
    def to_string(self):
        list_str = "[ "
        ptr = self.top
        while ptr != None       :
            list_str += str(ptr.val) + " "
            ptr = ptr.next
        return list_str + "]"

    # プッシュ
    def push(self, cell):
        if self.top != None:
            cell.next = ptr.next
        ptr.next = cell
        
    # 要素の取得
    def pop(self):
        # スタックが空の場合
        if self.top == None:
            return None
        

        # 一番上の要素を取り出す
        e = self.top
        self.top = e.next

        # 取り出す要素のポインタを初期化
        e.next = None

        return e

if __name__ == "__main__":
    S = Stack()
    S.push(Cell(2))
    S.push(Cell(8))
    S.push(Cell(5))
    print(S.pop().val)
    S.push(Cell(4))
    print(S.pop().val)
    print(S.pop().val)
    S.push(Cell(7))
    S.push(Cell(6))
    print("配列の状態")
    print(S.to_string())
    print("top の要素")
    print(S.top.val)


# In[ ]:





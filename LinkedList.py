#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

# 連結リストの各セル
class Cell:
    def __init__(self, val):
        self.val = val      # 要素が持つ値
        self.next = None    # 次のセルへのポインタ

# 連結リスト
class LinkedList:
    def __init__(self):
        self.head = None    # 先頭セル
        self.tail = None    # 末尾セル

    # リストの内部を表示する関数
    def to_string(self):
        list_str = "[ "
        ptr = self.head
        while ptr != None       :
            list_str += str(ptr.val) + " "
            ptr = ptr.next
        return list_str + "]"

    # 末尾へのセルの追加
    def append(self, cell):
        if self.head is None:
            # リストが空なら先頭に要素を追加
            self.head = cell
            self.tail = cell
        else:
            # リストの最後尾に要素を追加
            self.tail.next = cell
            self.tail = cell

    # 要素の取得
    def get(self, index):
        # インデックスの要素まで移動
        ptr = self.head
        for i in range(0, index):
            ptr = ptr.next

        return ptr

    # 要素の挿入
    def insert(self, index, cell):
        ptr = self.get(index-1)
        if ptr.next == None:
            self.append(cell)
        else:
            cell.next = ptr.next
            ptr.next = cell
        ## TODO:

    # 要素の削除 (削除されるのは cell の直後のセル)
    def delete(self, cell):
        if cell.next == None:
            return
        if cell.next.next == None:
            self.tail = cell
            
        cell.next = cell.next.next
        ## TODO:

if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.append(Cell(5))
    linkedlist.append(Cell(10))
    linkedlist.insert(1,Cell(3))
    linkedlist.append(Cell(12))

    print("リストの状態1")
    print(linkedlist.to_string())

    # index=2 のセルを削除
    y = linkedlist.get(1)
    linkedlist.delete(y)

    print("リストの状態2")
    print(linkedlist.to_string())

    # index=2 のセルを削除
    y = linkedlist.get(1)
    linkedlist.delete(y)

    print("リストの状態3")
    print(linkedlist.to_string())

    print("リストの先頭の値")
    print(linkedlist.head.val)
    print("リストの末尾の値")
    print(linkedlist.tail.val)


# In[ ]:





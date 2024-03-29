from collections import deque

# 木構造を表すデータ構造のためのクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(tree, node, i, n):
    if n > i:
        if tree[i] is None:
            return None
        temp = TreeNode(tree[i])
        node = temp
        node.left = make_tree(tree, node.left, 2 * i + 1, n)
        node.right = make_tree(tree, node.right, 2 * i + 2, n)

    return node

def main():
    N = int(input())
    tree = [int(N) for N in input().split()]

    # 二分木を深さ優先探索で探索する
    # 答えを入れるためのリスト
    ans = []
    # 木を作成
    root = make_tree(tree, None, 0, len(tree))
    # 答えを入れるためのリスト
    ans = []
    # スタックというデータ構造にリストを変換
    stack = deque([root])

    # 深さ優先探索の開始
    #stackが空にならない限りループを続ける
    while stack:
        #stackの右側から要素を一つ取り出す
        node = stack.pop()
        #ans（答え）に追加
        ans.append(node.val)
        #もし右側のノードが存在するならstackに追加
        if node.right:
            stack.append(node.right)
        #もし右側のノードが存在するならstackに追加
        if node.left:
            stack.append(node.left)
        print(ans)     

if __name__ == "__main__":
    main()
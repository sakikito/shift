from collections import deque

# 与えられる迷路の設定です
# 1 : 行き止まり
# 0 : 移動できる
N = int(input("行数> "))
print(str(N)+"行の迷路を書く")
print("1 : 行き止まり, 0 : 通行可と対応させる")
print("以下空白で区切って迷路を完成させてください>")
maze = [list(map(int, input().split())) for _ in range(N)]

print("start地点の要素番号を空白で区切って書いてください")
start = [int(s) for s in input().split()]

print("goal地点の要素番号を空白で区切って書いてください")
goal = [int(g) for g in input().split()]

# 深さ優先探索のためのスタック
stack = deque([start])
# 移動できる方向をまとめておく                            
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] 
# スタートを探索済みに変える  
maze[start[0]][start[1]] = int(1)      

# 幅優先探索開始
while stack:      
    # 現在地の座標を取り出す                                
    x, y = stack.popleft()
    # もしgoalの座標と現在地の座標が一致するなら
    if x == goal[0] and y == goal[1]:  
        # 1を表示してループを抜ける           
        print(1)                                  
        break
    # 右、左、上、下に行けるかどうかを判定する
    for dx, dy in directions:              
        # 現在地を次の地点に進める       
        nx = x + dx
        ny = y + dy                   
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == int(0):
            # もし次の地点が壁でない、かつ、迷路の外でないならば
            stack.append([nx, ny])                
            # キューに次に地点を追加して、探索済みにマーク
            maze[nx][ny] = int(1)
            print(maze)  
                                 
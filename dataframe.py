import pandas as pd
import random
from collections import deque

# 空のdataframeの作成(テトリス画面)
empty = pd.DataFrame()
print(empty)

# 出勤できる日と希望休のデータをランダムに作成
# 0 : 出勤
# 1 : 公休
day = int(input("日付>"))
people = int(input("人数>"))
shift = [list(random.randint(0, 1) for i in range(day)) for _ in range(people)]
print(shift)

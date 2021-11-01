import pandas as pd
from collections import defaultdict

res = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
file2 = 'loc.csv'
df2 = pd.read_csv(file2, names=['A', 'B'])
dict = defaultdict()
for i in range(1, 5077):
    if int(df2['B'][i]) > -1:
        res[int(df2['B'][i])] += 1
    else:
        res[15] += 1

print(res)
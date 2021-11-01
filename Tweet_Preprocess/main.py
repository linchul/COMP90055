# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import matplotlib.pyplot as plt
import plotly_express as px
from tqdm import tqdm, tqdm_notebook

locator = Nominatim(user_agent="myGeocoder")

file = 'geo-tweets.csv'
df = pd.read_csv(file, names=['A', 'B', 'X', 'Y'])  # 读取训练数据
print(df.shape)  # (189, 9)
dict_id = {}
for i in range(1, 30797):
    if df['A'][i] in dict_id.keys():
        continue
    else:
        dict_id[df['A'][i]] = df['Y'][i] + ',' + df['X'][i]
pd.DataFrame.from_dict(dict_id, orient='index').to_csv('user.csv')

file2 = 'user.csv'
df2 = pd.read_csv(file2, names=['A', 'B', 'address'])
locator = Nominatim(user_agent='myGeocoder', timeout=250)
rgeocode = RateLimiter(locator.reverse)

tqdm.pandas()

df2['address'] = df2['B'][1:].progress_apply(rgeocode)
##print(df2['address'][2].raw["address"]["suburb"])
print(df2['address'][2].raw['address']['state'])

dict = {}
for i in range(1, 5077):
    if df2['A'][i] in dict.keys():
        continue
    else:
        dict[df2['A'][i]] = df2['address'][i].raw['address']
pd.DataFrame.from_dict(dict, orient='index').to_csv('loc.csv')

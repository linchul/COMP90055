#!/usr/bin/python
import shapefile
from shapely.geometry import shape, Point
import pandas as pd

# read your shapefile
r = shapefile.Reader("GCCSA_2016_AUST.shp")

# get the shapes
shapes = r.shapes()

# build a shapely polygon from your shape

print(len(shapes))


def check(lon, lat):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    for i in range(0, 16):
        if shape(shapes[i]).contains(point):
            return i
    # the contains function does exactly what you want
    return -1


file2 = 'user1.csv'
df2 = pd.read_csv(file2, names=['A', 'B'])

dict = {}
for i in range(1, 2488):
    if df2['A'][i] in dict.keys():
        continue
    else:
        A = str.split(df2['B'][i][1:-1], ',')

        dict[df2['A'][i]] = check(float(A[1]), float(A[0]))
        print(i)
pd.DataFrame.from_dict(dict, orient='index').to_csv('loc1.csv')

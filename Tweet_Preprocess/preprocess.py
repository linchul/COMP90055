import shapefile
from shapely.geometry import shape, Point
import re
import pandas as pd
import json

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


file2 = 'tweet.txt'
file = open('tweet.txt')
dict = {}
try:
    text_lines = file.readlines()
    print(type(text_lines))

    for line in text_lines:
        id = re.findall(r'"id": (.*), "geo"', line)
        if id[0] not in dict:
            position = re.findall(r'"geo": (.*)}', line)
            dict[id[0]] = position[0]
finally:
    file.close()

print(len(dict.keys()))
pd.DataFrame.from_dict(dict, orient='index').to_csv('user1.csv')

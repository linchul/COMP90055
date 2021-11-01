#!/usr/bin/env python
# encoding: utf-8
import json
import time
import shapefile
from shapely.geometry import shape, Point

# read your shapefile
r = shapefile.Reader("../ll2name/GCCSA_2016_AUST.shp")

# get the shapes
shapes = r.shapes()
filename = "stat_data/0905_1005_geo.txt"
filename2 = "stat_data/" + filename.split(".")[0].split("/")[1] + "_geo2placeid." + filename.split(".")[1]

file_cnt = 0
geo_dict = {}

def check(lon, lat):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    for i in range(0,16):
        if shape(shapes[i]).contains(point):
            return i
    # the contains function does exactly what you want
    return -1

def stat_geo(filename, filename2,file_cnt = 0,file2_cnt = 0,geo_dict = {}):
    with open(filename, 'r') as obj:
        for line in obj.readlines():
            geo_dict = json.loads(line)

    print("dict size",len(geo_dict))
    new_dict = {}
    cnt = 0
    with open(filename2, 'w') as file2:
        for k,v in geo_dict.items():
            cnt += 1
            if cnt % 100 == 0:
                print('cnt:'+str(cnt))
            geo = eval(k)
            place_id = check(geo[1],geo[0])
            new_dict[k] = {}
            new_dict[k]['count'] = v
            new_dict[k]['place_id'] = place_id
            break
        json_line = json.dumps(new_dict)
        file2.write(json_line+'\n')
        file2_cnt += 1
        # if file2_cnt % 100 == 0:
        #     print('file2:'+str(file2_cnt))
start = time.time()
stat_geo(filename,filename2)
end = time.time()
print("total cost: ")
print(end-start)


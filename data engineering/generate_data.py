import json
import shapefile
from shapely.geometry import shape, Point

# read your shapefile
r = shapefile.Reader("../ll2name/GCCSA_2016_AUST.shp")

# get the shapes
shapes = r.shapes()

filename = "data_merge/0905_1005.txt"
filename2 = "stat_data/" + filename.split(".")[0].split("/")[1] + "." + filename.split(".")[1]
filename3 = "stat_data/0905_1005_geo_geo2placeid.txt"

def check(lon, lat):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    for i in range(0,16):
        if shape(shapes[i]).contains(point):
            return i
    # the contains function does exactly what you want
    return -1

#get placeid dict
#size 4904
with open(filename3, 'r') as obj3:
    for line in obj3.readlines():
        place2id = json.loads(line)
    # print(len(place2id))
file2_cnt = 0
# geo_dict = {}
with open(filename, 'r') as obj:
    with open(filename2, 'w') as file2:
        for line in obj.readlines():
            tweet = json.loads(line)
            user_id = tweet['user']['id']
            text = tweet['text']
            user = tweet['user']
            geo = tweet['geo']
            if str(geo) in place2id:
                place_id = place2id[str(geo)]["place_id"]
            else:
                place_id = check(geo[1],geo[0])
                place2id[str(geo)] = place_id
            new_dict = {}
            new_dict['id'] = user_id
            new_dict['text'] = text
            new_dict['user'] = user
            new_dict['place_id'] = place_id
            json_line = json.dumps(new_dict)
            file2.write(json_line+'\n')
            file2_cnt += 1
            if file2_cnt % 100 == 0:
                print('file2:'+str(file2_cnt))
import json
import shapefile
from shapely.geometry import shape, Point

# read your shapefile
r = shapefile.Reader("../ll2name/GCCSA_2016_AUST.shp")

# get the shapes
shapes = r.shapes()

filename = "stat_data/0905_1005.txt"
# filename2 = "stat_data/" + filename.split(".")[0].split("/")[1] + "." + filename.split(".")[1]
filename3 = "stat_data/0905_1005_multiplace_user.txt"
#filename4 store user and main placeid
filename4 = "stat_data/0905_1005_user_mainplaceid.txt"
#filename5 store user and placeid distribution
filename5 = "stat_data/0905_1005_user_placeid_distribution.txt"

def check(lon, lat):
    # build a shapely point from your geopoint
    point = Point(lon, lat)
    for i in range(0,16):
        if shape(shapes[i]).contains(point):
            return i
    # the contains function does exactly what you want
    return -1

file2_cnt = 0
user_dict = {}
user_multiplace_dict = {}
user_id_cnt = {}
user_mainid = {}
#to detect how many user tweet from different places
def detect_multiplace_user(filename,filename3):

    with open(filename, 'r') as obj:
        with open(filename3, 'w') as file3:
            for line in obj.readlines():
                tweet = json.loads(line)
                user_id = tweet['id']
                text = tweet['text']
                user = tweet['user']
                place_id = tweet['place_id']
                if user_id not in user_dict:
                    user_dict[user_id] = {}
                    user_dict[user_id]['place_id'] = {place_id}
                else:
                    if place_id not in user_dict[user_id]['place_id']:
                        user_dict[user_id]['place_id'].add(place_id)
                        user_multiplace_dict[user_id] = 1
            json_line = json.dumps(user_multiplace_dict)
            file3.write(json_line+'\n')
            # 3047个作者
            print(len(user_dict))
            # 356个作者在多地发推特
            print(len(user_multiplace_dict))

def get_main_placeid(filename,filename4,filename5):
    with open(filename, 'r') as obj:
        with open(filename5, 'w') as file5:
            for line in obj.readlines():
                tweet = json.loads(line)
                user_id = tweet['id']
                place_id = tweet['place_id']
                if user_id in user_multiplace_dict:
                    if user_id in user_id_cnt:
                        if place_id in user_id_cnt[user_id]:
                            user_id_cnt[user_id][place_id] += 1
                        else:
                            user_id_cnt[user_id][place_id] = 1
                    else:
                        user_id_cnt[user_id] = {}
                        user_id_cnt[user_id][place_id] = 1
            json_line = json.dumps(user_id_cnt)
            file5.write(json_line+'\n')

    for user_id, inner in user_id_cnt.items():
        max_cnt = 0
        max_place_id = -2
        for place_id,cnt in inner.items():
            if cnt > max_cnt:
                max_cnt = cnt
                max_place_id = place_id
        user_mainid[user_id] = {}
        user_mainid[user_id]["place_id"] = max_place_id
        user_mainid[user_id]["id_cnt"] = max_cnt

    with open(filename4, 'w') as file4:
        json_line = json.dumps(user_mainid)
        file4.write(json_line+'\n')





#detect which users tweet in multiple places.
detect_multiplace_user(filename,filename3)
get_main_placeid(filename,filename4,filename5)

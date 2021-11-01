import json
import shapefile
from shapely.geometry import shape, Point
#该文件需要将0905_1005.txt根据0905_1005_user_mainplaceid.txt该文件进行过滤，将主要的place_id的text消息合并
#其余的舍弃



filename = "stat_data/0905_1005.txt"
filename2 = "stat_data/0905_1005_user_mainplaceid.txt"
filename3 = "train_dev_data/0905_1005.txt"


file2_cnt = 0
user_dict = {}
user_multiplace_dict = {}
user_id_cnt = {}
user_mainid = {}
#to detect how many user tweet from different places
def generate_train_dev(filename,filename2,filename3):

    with open(filename2, 'r') as obj2:
        for line in obj2.readlines():
            user_mainid = json.loads(line)

    new_dict = {}
    with open(filename, 'r') as obj:
        with open(filename3, 'w') as file3:
            for line in obj.readlines():
                tweet = json.loads(line)
                user_id = tweet['id']
                text = tweet['text']
                user = tweet['user']
                place_id = tweet['place_id']
                #check 用户是否在多个地方发送tweet
                if user_id in user_mainid:
                    #命中
                    if place_id == user_mainid[user_id]['place_id']:
                        if user_id in new_dict:
                            new_dict[user_id]['text'] += text
                        else:
                            new_dict[user_id] = {}
                            new_dict[user_id]['text'] = text
                            new_dict[user_id]['user'] = user
                            new_dict[user_id]['place_id'] = place_id
                    else:
                        continue
                else:
                    if user_id in new_dict:
                        new_dict[user_id]['text'] += text
                    else:
                        new_dict[user_id] = {}
                        new_dict[user_id]['text'] = text
                        new_dict[user_id]['user'] = user
                        new_dict[user_id]['place_id'] = place_id

            json_line = json.dumps(new_dict)
            #3047
            print(len(new_dict))
            file3.write(json_line+'\n')

generate_train_dev(filename,filename2,filename3)

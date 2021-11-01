import json
import shapefile
from shapely.geometry import shape, Point
#该文件需要将0905_1005.txt根据0905_1005_user_mainplaceid.txt该文件进行过滤，将主要的place_id的text消息合并
#其余的舍弃



filename = "ori_data/lzn_wyb_0905_ori.txt"
filename2 = "test_data/0905.txt"


file2_cnt = 0
user_dict = {}
user_multiplace_dict = {}
user_id_cnt = {}
user_mainid = {}
#to detect how many user tweet from different places
def generate_test(filename,filename2):

    user_dict = {}
    cnt = 0
    with open(filename, 'r') as obj:
        with open(filename2, 'w') as file2:
            for line in obj.readlines():
                tweet = json.loads(line)
                user_id = tweet['user']['id']
                text = tweet['text']
                user = tweet['user']
                location = tweet['location']
                #check 用户是否在多个地方发送tweet
                if user_id in user_dict:
                    #命中
                    user_dict[user_id]['text'] += text
                else:
                    user_dict[user_id] = {}
                    user_dict[user_id]['text'] = text
                    user_dict[user_id]['user'] = user
                    user_dict[user_id]['location'] = location
                cnt += 1
                if cnt % 1000 == 0:
                    print(cnt)
            json_line = json.dumps(user_dict)
            #3047
            print('test user cnt: ',len(user_dict))
            file2.write(json_line+'\n')

generate_test(filename,filename2)

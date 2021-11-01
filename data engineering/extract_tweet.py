import json

filename = "raw_data/lzn_wyb_1005.txt"
filename2 = "ori_data/" + filename.split(".")[0].split("/")[1] + "_ori." + filename.split(".")[1]
filename3 = "new_data/" + filename.split(".")[0].split("/")[1] + "_new." + filename.split(".")[1]
file3_cnt = 0
file2_cnt = 0
print(filename2)
with open(filename, 'r') as obj:
    with open(filename3, 'w') as file3,\
            open(filename2,'w') as file2:
        for line in obj.readlines():
            tweet = json.loads(line)
            geo = tweet['geo']
            if geo:
                id = tweet['id']
                text = tweet['text']
                user = tweet['user']
                coordinates = tweet['coordinates']
                new_dict = {}
                new_dict['id'] = id
                new_dict['text'] = text
                new_dict['user'] = user
                new_dict['geo'] = geo['coordinates']
                json_line = json.dumps(new_dict)
                file3.write(json_line+'\n')
                file3_cnt += 1
                if file3_cnt % 100 == 0:
                   print('file3:'+str(file3_cnt))
            else:
                id = tweet['id']
                text = tweet['text']
                user = tweet['user']
                coordinates = tweet['coordinates']
                new_dict = {}
                new_dict['id'] = id
                new_dict['text'] = text
                new_dict['user'] = user
                # new_dict['geo'] = geo['coordinates']
                new_dict['location'] = user['location']
                json_line = json.dumps(new_dict)
                # print(json_line)
                # break
                file2.write(json_line+'\n')
                file2_cnt += 1
                if file2_cnt % 100 == 0:
                    print('file2:'+str(file2_cnt))

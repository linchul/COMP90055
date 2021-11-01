import json

filename = "data_merge/0905_1005.txt"
filename3 = "linchu/" + filename.split(".")[0].split("/")[1] + "." + filename.split(".")[1]
file3_cnt = 0
# file2_cnt = 0
print(filename3)
with open(filename, 'r') as obj:
    with open(filename3, 'w') as file3:
        for line in obj.readlines():
            tweet = json.loads(line)
            id = tweet['user']['id']
            geo = tweet['geo']
            new_dict = {}
            new_dict['id'] = id
            new_dict['geo'] = geo
            json_line = json.dumps(new_dict)
            file3.write(json_line+'\n')
            file3_cnt += 1
            if file3_cnt % 100 == 0:
                print('file3:'+str(file3_cnt))

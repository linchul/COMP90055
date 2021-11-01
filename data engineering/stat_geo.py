import json

filename = "data_merge/0905_1005.txt"
filename2 = "stat_data/" + filename.split(".")[0].split("/")[1] + "_geo." + filename.split(".")[1]

file_cnt = 0
geo_dict = {}


def stat_geo(filename, filename2,file_cnt = 0,file2_cnt = 0,geo_dict = {}):
    with open(filename, 'r') as obj:
        for line in obj.readlines():
            tweet = json.loads(line)
            geo = tweet['geo']
            geo_dict[str(geo)] = geo_dict.get(str(geo), 0) + 1
            file_cnt += 1
            if file_cnt % 100 == 0:
                print('file2:' + str(file_cnt))
    print("dict size",len(geo_dict))
    with open(filename2, 'w') as file2:
        json_line = json.dumps(geo_dict)
        # print(json_line)
        # break
        file2.write(json_line+'\n')
        file2_cnt += 1
        if file2_cnt % 100 == 0:
            print('file2:'+str(file2_cnt))

stat_geo(filename,filename2)


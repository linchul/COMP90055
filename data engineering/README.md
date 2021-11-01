# data engineering

### part1 extract tweet data
{user_id, text, user_information, geo}
* extract_tweet.py: 
  Extract the data from the original Twitter data and divide the geo-tagged and non-geo-tagged data
  
### part2 Convert geo coordinates to specific place id
{user_id, text, user_information, place_id}
* stat_geo.py:
  Extract all geographic coordinates and store them in a file
* stat_geo2placeid.py:
  Convert the specific geographic location coordinates to the place id corresponding to the GCCSA standard
* run_stat_gep2placeid.sh:
  Run stat_geo2placeid.py.Because this part is time-consuming, the files is executed on the server.
* generate_data.py:
  Using the mapping relationship between the geographic location and the place id stored in stat_geo2placeid.py, we run 
  this file to replace the geographic location in the Twitter data with the corresponding place id
* GCCSA_2016_AUST.shp：
  This is the GCCSA standard document

### part3 Filter multiple place IDs for the same user
{user_id, merged text, user_information, place_id}
* filter_multiplaceid.py:
  This file first counts which users will send Twitter messages in different locations. Then  the place is used where 
  these users most frequently send Twitter messages as the user's place id. At the same time, the Twitter messages sent 
  by the same user are merged, and in this process, the messages which are sent at the place id that are not frequently 
  sent by the above-mentioned users are filtered.

### part4 Construct train dataset
{user_id, text, user_information, place_id}
* construct_train.py:
  construct the train dataset
* construct_test.py:
  construct the test dataset

### prepare for downstream population prediction
* extract_tweet2linchu.py: 
  Extract user id and geographic location to prepare for downstream population prediction





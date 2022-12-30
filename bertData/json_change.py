import pandas as pd
# df = pd.read_json('./YOUR_FILENAME_EMOTIONS.json')
# lens = df.__len__()
# print(df.get("text"),df.get("surprise").sum()/lens)

# def get_average(js,len):
#     sums = 0
#     for i in range(len):
#         sums += float(js.get(str(i)))
#     return str(round((sums/len)*100,3))+"%"
#
# import json
# with open('./YOUR_FILENAME_EMOTIONS.json',encoding='utf-8-sig', errors='ignore') as json_file:
#     data = json.load(json_file)
# print(data)
#
# print("surprise :",get_average(data.get("surprise"),len(data.get("surprise"))))
# print("anger :",get_average(data.get("anger"),len(data.get("anger"))))
# print("disgust :",get_average(data.get("disgust"),len(data.get("disgust"))))
# print("fear :",get_average(data.get("fear"),len(data.get("fear"))))
# print("joy :",get_average(data.get("joy"),len(data.get("joy"))))
# print("neutral :",get_average(data.get("neutral"),len(data.get("neutral"))))
# print("sadness :",get_average(data.get("sadness"),len(data.get("sadness"))))

# import codecs
# import csv
#
# with codecs.open('./YOUR_FILENAME_EMOTIONS.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
# print(data)
#
# data = pd.read_json('the_belt_and_road.json')
import json
with open('./Beijing Winter Olympics.json',encoding='utf-8-sig', errors='ignore') as json_file:
    data = json.load(json_file)
print(data[0]["comment"][1]["text"])     #data[0]["comment"][0]["text"]
print(len(data[2]["comment"]))
print(len(data))


import pandas as pd
from tabulate import tabulate
#对写出的csv文件进行解析
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

data = pd.read_csv('YOUR_FILENAME_EMOTIONS.csv')
print("Average of “joy” Emotion:",data["joy"].sum()/len(data["joy"]))
max_index  = list(data["joy"]).index(max(data["joy"]))   #获得最喜悦的索引
print("MAX “joy” Emotion：",max(data["joy"]))      #打印出最喜悦的索引
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of “sadness” Emotion:",data["sadness"].sum()/len(data["sadness"]))
max_index  = list(data["sadness"]).index(max(data["sadness"]))   #获得最喜悦的索引
print("MAX “sadness” Emotion：",max(data["sadness"]))      #打印出最悲伤的索引
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of “surprise” Emotion:",data["surprise"].sum()/len(data["sadness"]))
max_index  = list(data["surprise"]).index(max(data["surprise"]))   #获得最惊喜的索引
print("MAX “surprise“ Emotion：",max(data["surprise"]))      #打印出最惊奇的索引
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of ”disgust“ Emotion:",data["disgust"].sum()/len(data["disgust"]))
max_index  = list(data["disgust"]).index(max(data["disgust"]))
print("MAX ”disgust“ Emotion：",max(data["disgust"]))
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of ”neutral“ Emotion:",data["neutral"].sum()/len(data["neutral"]))
max_index  = list(data["neutral"]).index(max(data["neutral"]))
print("MAX ”neutral“ Emotion：",max(data["neutral"]))
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of ”fear“ Emotion:",data["fear"].sum()/len(data["fear"]))
max_index  = list(data["fear"]).index(max(data["fear"]))
print("MAX ”fear“ Emotion：",max(data["fear"]))
print("counterPart comment：",data["text"].get(max_index))
print("----------------------------------------------------------------------------------------------")
print("Average of ”anger“ Emotion:",data["anger"].sum()/len(data["anger"]))
max_index  = list(data["anger"]).index(max(data["anger"]))
print("MAX ”anger“ Emotion：",max(data["anger"]))
print("counterPart comment：",data["text"].get(max_index))
print()
print()
table = [['Emotion_name', 'Max_emotion', 'Ave_Emotion'],
['joy',max(data["joy"]), data["joy"].sum()/len(data["joy"])],
['sadness',max(data["sadness"]) , data["sadness"].sum()/len(data["sadness"])],
['neutral',max(data["neutral"]), data["neutral"].sum()/len(data["neutral"])],
         ['surprise',max(data["surprise"]), data["surprise"].sum()/len(data["surprise"])],
         ['disgust',max(data["disgust"]) , data["disgust"].sum()/len(data["disgust"])],
         ['fear',max(data["fear"]) , data["fear"].sum()/len(data["fear"])],
         ['anger',max(data["anger"]), data["anger"].sum()/len(data["anger"])]]
print(tabulate(table, headers='firstrow'))

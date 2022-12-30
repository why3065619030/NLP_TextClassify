import json
import csv
import pandas
from datetime import *
now = datetime.now()

"""
需求：将json中的数据转换成csv文件
"""
def csv_json(name):
    # 1.分别 读，创建文件
    json_fp = open(name+".json", "r",encoding='utf-8')
    datas = json.load(json_fp)  #datas[0] == 22,data[0][0]["comment"][1]["text"]
    comments = []
    time = []
    for i in range(len(datas)):
        for j in range(len(datas[i]["comment"])):
            #时间可能出现'3年前（修改过）'，需要清洗
            t = datas[i]["comment"][j]["time"]
            if '（修改过）' in t:
                t = t.replace('（修改过）', '')
            if '天' in t:
                day,st = t.split('天')
                t = int(day)
            elif '周' in t:
                week,st = t.split('周')
                t = int(week)*7
            elif '月' in t:
                month,st = t.split('个')
                t = int(month)*30
            elif '年' in t:
                year,st = t.split('年')
                t = int(year)*365
            else:
                t = 0
            y = now + timedelta(days=-t)  # 昨天
            comments.append(datas[i]["comment"][j]["text"])
            time.append(str(y.date()))
    print(len(datas))
    print(comments[0])
    print(time[0])

    data = pandas.DataFrame({'text':comments,"time":time})
    data.to_csv(name+".csv",index=False)

    json_fp.close()



def changeData(name):
    csv_json("./Data/"+name)

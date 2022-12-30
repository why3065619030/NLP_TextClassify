import pandas as pd
from tabulate import tabulate
import pandas as pd
import time
import datetime
from tabulate import tabulate
from collections import defaultdict
dict = defaultdict(list)

import pymysql

def insert_db(insert_sql):
    """插入"""
    # 建立数据库连接
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="sys"
    )
    # 通过 cursor() 创建游标对象
    cur = db.cursor()
    try:
        # 使用 execute() 执行sql
        cur.execute(insert_sql)
        # 提交事务
        db.commit()
    except Exception as e:
        print("操作出现错误：{}".format(e))
        # 回滚所有更改
        db.rollback()
    finally:
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        db.close()

def do(emotionAnaId):
    data = pd.read_csv('./bertData/YOUR_FILENAME_EMOTIONS.csv') #相对于main函数的路径
    l = data["label"]
    times = data["time"].dropna().astype('str').tolist()
    types = set(times)
    list = []
    for date_str in types:  # 将字符串组装成data类型
        fmt = '%Y-%m-%d'
        time_tuple = time.strptime(date_str, fmt)
        year, month, day = time_tuple[:3]
        a_date = datetime.date(year, month, day)
        list.append(a_date)
    list = sorted(list)  # 按照日期从小到大

    for index, t in enumerate(times):
        dict[t].append(index)  # 将日期存在字典中

    # f = open('./tmp_trainer/'+name+'.txt', 'w')
    # 整体
    # for date in list:
    #     Sum = len(l)  # 总评论数目
    #     anger = 0
    #     disgust = 0
    #     fear = 0
    #     joy = 0
    #     neutral = 0
    #     sadness = 0
    #     surprise = 0
    #     for i in l:
    #         if i == "anger":
    #             anger += 1
    #         elif i == "disgust":
    #             disgust += 1
    #         elif i == "fear":
    #             fear += 1
    #         elif i == "joy":
    #             joy += 1
    #         elif i == "neutral":
    #             neutral += 1
    #         elif i == "sadness":
    #             sadness += 1
    #         else:
    #             surprise += 1
    #
    # f.write("整体" + '\n')
    # f.write("anger " + "disgust " + "fear " + "joy " + "neutral " + "sadness " + "surprise "+"Sum " + '\n')
    # f.write(str(anger) + " " + str(disgust) + " " + str(fear) + " " + str(joy) + " " + str(neutral) + " " + str(
    #     sadness) + " " + str(surprise) + " " + str(Sum) + '\n')
    # f.write("生气：" + str("%.2f" % (anger * 100.0 / Sum)) + "%" + '\n')
    # f.write("厌恶：" + str("%.2f" % (disgust * 100.0 / Sum)) + "%" + '\n')
    # f.write("恐惧：" + str("%.2f" % (fear * 100.0 / Sum)) + "%" + '\n')
    # f.write("喜悦：" + str("%.2f" % (joy * 100.0 / Sum)) + "%" + '\n')
    # f.write("中立：" + str("%.2f" % (neutral * 100.0 / Sum)) + "%" + '\n')
    # f.write("悲伤：" + str("%.2f" % (sadness * 100.0 / Sum)) + "%" + '\n')
    # f.write("惊喜：" + str("%.2f" % (surprise * 100.0 / Sum)) + "%" + '\n')
    # f.write('\n')
    # 按日期
    # f.write("按日期升序" + '\n')
    for date in list:
        Sum = len(dict[str(date)])  # 总评论数目
        anger = 0
        disgust = 0
        fear = 0
        joy = 0
        neutral = 0
        sadness = 0
        surprise = 0
        for i in dict[str(date)]:
            if l[i] == "anger":
                anger += 1
            elif l[i] == "disgust":
                disgust += 1
            elif l[i] == "fear":
                fear += 1
            elif l[i] == "joy":
                joy += 1
            elif l[i] == "neutral":
                neutral += 1
            elif l[i] == "sadness":
                sadness += 1
            else:
                surprise += 1

        if Sum:
            insert_sql = 'INSERT INTO 7classify(emotionAnaid, anger,disgust,fear,joy,neutral,sadness,surprise,time) VALUES(' + str(
                emotionAnaId) + ',' + str(
                anger) + ',' + str(disgust) + ',' + str(fear) + ',' + str(joy) + ',' + str(neutral) + ',' + str(
                sadness) + ',' + str(
                surprise) + ',' + '"' + str(date) + '")'
            insert_db(insert_sql)
            # f.write(str(date) + '\n')
            # f.write("anger " + "disgust " + "fear " + "joy " + "neutral " + "sadness " + "surprise " +"Sum"+ '\n')
            # f.write(str(anger) + " " + str(disgust) + " " + str(fear) + " " + str(joy) + " " + str(neutral) + " " + str(
            #     sadness) + " " + str(surprise) + " " + str(Sum) + '\n')
            # f.write("生气：" + str("%.2f" % (anger * 100.0 / Sum)) + "%" + '\n')
            # f.write("厌恶：" + str("%.2f" % (disgust * 100.0 / Sum)) + "%" + '\n')
            # f.write("恐惧：" + str("%.2f" % (fear * 100.0 / Sum)) + "%" + '\n')
            # f.write("喜悦：" + str("%.2f" % (joy * 100.0 / Sum)) + "%" + '\n')
            # f.write("中立：" + str("%.2f" % (neutral * 100.0 / Sum)) + "%" + '\n')
            # f.write("悲伤：" + str("%.2f" % (sadness * 100.0 / Sum)) + "%" + '\n')
            # f.write("惊喜：" + str("%.2f" % (surprise * 100.0 / Sum)) + "%" + '\n')
            # f.write('\n')
    # f.close()
if __name__ == '__main__':
    do("Chinese Medicine")
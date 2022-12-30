import pandas as pd
import time
import datetime
from tabulate import tabulate
from collections import defaultdict

dict = defaultdict(list)
def do(name):
    data = pd.read_csv('./why.csv')
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

    f = open('./tmp_trainer/'+name+'.txt', 'w')
    # 整体
    for date in list:
        Sum = len(l)  # 总评论数目
        negativeSum = 0  # 消极评论
        positiveSum = 0  # 积极评论数
        for i in l:
            if i == "POSITIVE":
                positiveSum += 1
            else:
                negativeSum += 1

    f.write("整体" + '\n')

    f.write(str(negativeSum) + " " + str(positiveSum) + " " + str(Sum) + '\n')
    f.write("消极：" + str("%.2f" % (negativeSum * 100.0 / Sum)) + "%" + '\n')
    f.write("积极：" + str("%.2f" % (positiveSum * 100.0 / Sum)) + "%" + '\n')
    f.write('\n')
    # 按日期
    f.write("按日期升序" + '\n')
    for date in list:
        Sum = len(dict[str(date)])  # 总评论数目
        negativeSum = 0  # 消极评论数
        positiveSum = 0  # 积极评论数
        for i in dict[str(date)]:
            if l[i] == "POSITIVE":
                positiveSum += 1
            else:
                negativeSum += 1
        f.write(str(date) + '\n')
        f.write(str(negativeSum) + " " + str(positiveSum) + " " + str(Sum) + '\n')
        f.write("消极：" + str("%.2f" % (negativeSum * 100.0 / Sum)) + "%" + '\n')
        f.write("积极：" + str("%.2f" % (positiveSum * 100.0 / Sum)) + "%" + '\n')
        f.write('\n')
    f.close()
    # print(str(date))
    # print(negativeSum, positiveSum, Sum)
    # print("消极：", str("%.2f" % (negativeSum * 100.0 / Sum)) + "%")
    # print("积极：", str("%.2f" % (positiveSum * 100.0 / Sum)) + "%")
    # print()
if __name__ == '__main__':
    do("Beijing Winter Olympics")

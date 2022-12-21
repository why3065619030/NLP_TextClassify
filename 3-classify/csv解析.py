import pandas as pd
from tabulate import tabulate
data = pd.read_csv('./why.csv')
list = data["label"]
Sum = len(list)     #总评论数目
negativeSum = 0     #消极评论数
neutralSum = 0      #中立评论数
positiveSum = 0     #积极评论数
for i in list:
    if i == "POS":
        positiveSum += 1
    elif i == "NEU":
        neutralSum += 1
    else:
        negativeSum += 1
print(negativeSum,neutralSum,positiveSum,Sum)
print("消极：",str("%.2f"%(negativeSum*100.0/Sum))+"%")
print("中立：",str("%.2f"%(neutralSum*100.0/Sum))+"%")
print("积极：",str("%.2f"%(positiveSum*100.0/Sum))+"%")

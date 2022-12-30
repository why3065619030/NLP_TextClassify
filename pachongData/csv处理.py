import pandas as pd
from tabulate import tabulate
data = pd.read_csv('./20150218230000.export.CSV',sep="\t",names=[str(i) for i in range(61)])
#第31行GoldsteinScale指定该类事件对国家稳定的潜在影响
print(type(data))
print(data["30"])
#第35行AvgTone指定情感极性
print(data["34"])

import requests
import pandas as pd
import zipfile
import os

# masterfilelist = 'http://data.gdeltproject.org/gdeltv2/masterfilelist.txt'
with open('./masterfilelist.txt','r') as file:
    urls = file.readlines()
    urls = list(reversed(urls))
    file.close()
for url in urls:
    resp = requests.get('http://'+url.strip('\n'))
    if str(resp) == '<Response [200]>':
        zfname = '../pachongData/demo.zip'
        with open(zfname, "wb") as code:
            code.write(resp.content)
        with zipfile.ZipFile(zfname) as zf:
            zf.extractall(path='../pachongData')
    else:
        print('Request Error!')

# test1=pd.read_csv("../Data/20150218230000.export.csv",delimiter="\t",header=None)
# print(type(test1))
# print(test1[60].head())



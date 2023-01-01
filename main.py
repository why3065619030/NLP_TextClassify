import pymysql
from Sevenclass import SevClassify
from reptilian import Spider
from Sevenclass import csvOrJson
from bertData import jToC
from ThreeClassify import TClassify
from ThreeClassify import saveToDatabase
from LDA import lda
from Twoclassify import twoclassify
from Twoclassify import toDataset
def select_db(select_sql):
    """查询"""
    # 建立数据库连接
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="sys"    #数据库名字
    )
    # 通过 cursor() 创建游标对象，并让查询结果以字典格式输出
    cur = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute() 执行sql
    cur.execute(select_sql)
    # 使用 fetchall() 获取所有查询结果
    data = cur.fetchall()
    # 关闭游标
    cur.close()
    # 关闭数据库连接
    db.close()
    return data



def update_db(update_sql):
    """更新"""
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
        cur.execute(update_sql)
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


if __name__ == '__main__':
    keyword = input()  # 获取关键词
    Spider.getData(keyword)  # 数据保存在./Data/keyword.json
    # 将json转化为csv，并按日期升序
    jToC.changeData(keyword)
    # 读取csv文件，并进行情感分类

    TClassify.ThreeClass(keyword)   #3
    saveToDatabase.do(emotionAnaId=1)
    print("三分类已存")

    twoclassify.TwoClassify(keyword) #2
    toDataset.do(emotionAnaId=1)
    print("二分类已存")
    SevClassify.SevenClassify(keyword)  # 7结果保存在./bertData/YOUR_FILENAME_EMOTIONS.csv
    # 将7分类结果的csv文件分析并插入数据库
    csvOrJson.do(emotionAnaId=2)
    print("七分类已存")
    # lda.get_LDA(keyword)        #./Data/keyword.json处拿数据分析


# d = "2022-03-01"
# anger = 0
# disgust = 0
# fear = 0
# joy = 0
# neutral = 0
# sadness = 0
# surprise = 0
# date = "2020-12-01"
# insert_sql = 'INSERT INTO 7classify(emotionAnaid, anger,disgust,fear,joy,neutral,sadness,surprise,time) VALUES('+str(0)+',' + str(
#     anger) + ',' + str(disgust) + ',' + str(fear) + ',' + str(joy) + ',' + str(neutral) + ',' + str(sadness) + ',' + str(
#     surprise) + ',' + '"' + str(date) + '")'
# print(insert_sql)
# insert_db(insert_sql)


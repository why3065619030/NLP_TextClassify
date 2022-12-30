import requests
import json
import urllib3
import re
from jsonsearch import JsonSearch

urllib3.disable_warnings()



# 根据关键词获取视频号列表
def getVideoUrl(keyword):
    print("Getting video list......")
    search_url = "https://m.youtube.com/results?search_query=" + keyword
    resp = requests.get(search_url)
    if resp.status_code == 200:
        video_list = []
        result_json = re.findall(r'ytInitialData = (.*);</script>', resp.text)[0]
        result_obj = json.loads(result_json)
        js_data = JsonSearch(object=result_obj, mode='j')
        videoRendererList = js_data.search_all_value(key='videoRenderer')
        for videoRenderer in videoRendererList:
            video_list.append(videoRenderer['videoId'])
        return video_list
    else:
        return 500

# 获取爬取评论需要的视频口令
def getToken(video='j8zzL2aBo2M'):
    print("Getting token.............")
    headers = {
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35,gzip(gfe)",
    }
    token_url = 'https://www.youtube.com/watch?v={}&t=1s'.format(video)
    resp = requests.get(token_url, headers=headers)
    if resp.status_code == 200:
        result_json = re.findall(r'ytInitialData = (.*);</script>', resp.text)[0]
        json_data = JsonSearch(object=result_json, mode='s')
        token = json_data.search_first_value(key='token')
        return token
    else:
        return 500

# 获取视频其它评论所需的Token列表
def getNextToken(data):
    json_data = JsonSearch(object=data, mode='j')
    t = json_data.search_all_value(key='token')
    print(len(t))
    return t[1:]

# 爬取评论
def getComment(token):
    print("Getting comment..................")
    json_data = {
        "context": {
            "client": {
                "hl": "zh-CN",
                "gl": "US",
                "remoteHost": "203.75.191.37",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgtkM0h2anMza1JmSSidlL6bBg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20221110.08.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/watch?v=j8zzL2aBo2M",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CJ2UvpsGELKI_hIQ1IOuBRCHkf4SELiLrgUQm8quBRDiua4FEKmnrgUQuNSuBRDik_4SENi-rQUQkfj8Eg"
                                      "%3D%3D "
                },
                "screenDensityFloat": 1.25,
                "timeZone": "Asia/Shanghai",
                "browserName": "Edge Chromium",
                "browserVersion": "107.0.1418.35",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                                "application/signed-exchange;v=b3;q=0.9",
                "deviceExperimentId": "ChxOekUyTlRBNU56TTRPVFV3TlRjeE1EWTNNdz09EJ2UvpsG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 792,
                "utcOffsetMinutes": 480,
                "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
                "connectionType": "CONN_CELLULAR_4G",
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "https://www.youtube.com/watch?v=j8zzL2aBo2M",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_UNKNOWN",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": 'true'
                }
            },
            "user": {
                "lockedSafetyMode": 'false'
            },
            "request": {
                "useSsl": 'true',
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CPQCELsvGAMiEwj8u_upy6j7AhXBQoUKHTT2AK0="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1668254239799"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "480"
                    },
                    {
                        "key": "u_his",
                        "value": "5"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "864"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "792"
                    },
                    {
                        "key": "biw",
                        "value": "1519"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,864,1536,792"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "continuation": "Eg0SC2o4enpMMmFCbzJNGAYyJSIRIgtqOHp6TDJhQm8yTTAAeAJCEGNvbW1lbnRzLXNlY3Rpb24%3D"
    }
    json_data['continuation'] = token
    comment_list = []
    url = 'https://www.youtube.com/youtubei/v1/next?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
    resp = requests.post(url, json=json_data)
    data = json.loads(resp.text)
    js_data = JsonSearch(object=data, mode='j')
    c = js_data.search_all_value(key='contentText')
    p = js_data.search_all_value(key='publishedTimeText')
    if len(c) == len(p):
        for i in range(len(c)):
            comment = {}
            comment['text'] = c[i]['runs'][0]['text']
            comment['time'] = p[i]['runs'][0]['text']
            comment_list.append(comment)
    else:
        return comment_list
    print(len(comment_list))
    return comment_list

# 保存评论
def commentSave(data,keyword):
    print("Saving comment....................")
    with open('./Data/{}.json'.format(keyword), 'a', encoding='utf-8') as fp:
        json.dump(data, fp, indent=4, ensure_ascii=False)
        fp.close

#转换单一json文件
def change_json_tmp(name):
    json_p = name
    out_p = name
    with open(name+'.json', 'r', encoding='utf-8') as f:
        s = f.read()
    s = s.replace("][", ",") ##字符串正则转换
    json_out = json.loads(s)
    with open(name+'.json', 'w', encoding='utf-8') as f:
        json.dump(json_out, f)


def getData(word):
    keyword = word



    video_list = getVideoUrl(keyword=keyword)

    for video in video_list:
        comment_list = []
        comment = {'comment': getComment(getToken(video)), 'video': video}
        comment_list.append(comment)
        commentSave(comment_list,keyword=keyword)
    change_json_tmp('./Data/'+keyword)
    # getComment('Eg0SC2o4enpMMmFCbzJNGAYyJSIRIgtqOHp6TDJhQm8yTTAAeAJCEGNvbW1lbnRzLXNlY3Rpb24%3D')

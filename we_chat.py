import requests
import json
import time
def sendwx(content,sendKey):
    url = "https://pushbear.ftqq.com/sub"
    data={
        "sendkey": sendKey,
        "text": "听云华东告警平台",
        "desp":content
    }
    res = requests.post(url,data)
    # print(json.loads(res.text))
    return res
def sendwxnew(content,sendKey,title):
    url = "https://message-pro.mjjpipi.xyz/push"
    header={
        "content-type":"application/json"
    }
    data={
        "channelName": sendKey,
        "text": content,
        "title":title
    }
    res = requests.post(url,json.dumps(data),headers=header)
    # print(json.loads(res.text))
    return res
def send(content,sendKey,title,Type):
    url = "https://message.mjjpipi.xyz/push"
    header={
        "content-type":"application/json"
    }
    data={
        "channelName": sendKey,
        "text": content,
        "title":title,
        "Type": Type,
        "Time": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    }
    res = requests.post(url,json.dumps(data),headers=header)
    #print(json.loads(res.text))
    return res
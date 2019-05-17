import requests
import json
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
    url = "https://tingyun.leanapp.cn/push"
    header={
        "content-type":"application/json"
    }
    data={
        "channelName": sendKey,
        "text": content,
        "title":title
    }
    res = requests.post(url,json.dumps(data),headers=header)
    print(json.loads(res.text))
    return res
import requests
import json
def sendwx(content,sendKey,constumer):
    url = "https://pushbear.ftqq.com/sub"
    data={
        "sendkey": sendKey,
        "text": "听云告警-"+str(constumer),
        "desp":content
    }
    res = requests.post(url,data)
    # print(json.loads(res.text))
    return res
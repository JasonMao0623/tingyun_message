import requests
import json
def sendwx(content):
    url = "https://pushbear.ftqq.com/sub"
    data={
        "sendkey": "3288-cddd2195e76cfba892c071d7cfac279f",
        "text": "听云告警",
        "desp":content
    }
    res = requests.post(url,data)
    # print(json.loads(res.text))
    return res
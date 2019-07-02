import requests
import json
def send_message(content,wx_url,name):
    template = "#### 华东推送系统企业微信端\n**标题**:"+name+"\n**内容**:<font color='warning'>"+content+"</font>"
    url = wx_url
    header={
        "Content-Type":"application/json"
    }
    data={
        "msgtype": "markdown",
        "markdown":{
            "content":template
        }
    }
    res = requests.post(url,json.dumps(data),headers=header)
    print(json.loads(res.text))
    return res
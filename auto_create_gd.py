import requests
import json
s=requests.Session()
loginUrl="http://127.0.0.1/index.php/api/index/userLogin"
createUrl="http://127.0.0.1/index.php/api/index/createOrder"
checkStatus="http://127.0.0.1/index.php/api/index/getBaseOrderInfo"
# 登录工单获取session
def login():
    data={
        "password":"Sh123456",
        "login":"testn"
    }
    s.headers={
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"
    }
    res = s.post(loginUrl,data=data)
    if json.loads(res.text)["error_code"]==0:
        return True
    else:
        return False
# 创建工单
def create_gd(title,desc):
    data = {
        "title":title,
        "desc":desc,
        "service_id":"4",
        "product_id":"9",
        "question_id":"3",
        "attachment_id":""
    }
    isLoginIn=login()
    if isLoginIn:
        res=s.post(createUrl,data=data)
        print(res.text)
        if json.loads(res.text)["error_code"]==0:
            return "OK"


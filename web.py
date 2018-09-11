from flask import Flask,request
app =Flask(__name__)
import time
import log_out
import we_chat
def utils(content,sendkey,name):
    if content:
        we_chat.sendwx(content, sendkey)
        content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 推送成功 " + " 内容：" + content + "客户:"+name
        log_out.log_out(content_value)
    else:
        content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 推送失败 " + " 内容：" + content + "客户:"+name
        log_out.log_out(content_value)
        return "推送失败请确认请求参数", 500
    return "推送成功", 200
@app.route("/test/message",methods=["POST"])
# 测试环境方法
def test_dataProcess():
    if request.method =="POST":
        print(request.form)
        content = request.form["content"]
        key = str(request.form["key"])
        name = str(request.form["name"])
        res = utils(content,key,name)
        return  res
    else:
        return "请求方法为POST",500
@app.route("/huadong/message",methods=["POST"])
# 生产环境方法
def product_dataProcess():
    if request.method =="POST":
        print(request.form)
        content = request.form["content"]
        key = str(request.form["key"])
        name = str(request.form["name"])
        res = utils(content,key,name)
        return  res
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 8089,
    debug=True
)
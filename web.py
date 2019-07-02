from flask import Flask,request
app =Flask(__name__)
import time
import log_out
import we_chat
import qiye_wexin
def utils(content,sendkey,name,wx_url):
    if content:
        if wx_url:
            qiye_wexin.send_message(content, wx_url,name)
        else:
            we_chat.sendwxnew(content,sendkey,name)
        content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 推送成功 " + " 内容：" + content + "客户:"+name
        # log_out.log_out(content_value)
    else:
        content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 推送失败 " + " 内容：" + content + "客户:"+name
        # log_out.log_out(content_value)
        return "推送失败请确认请求参数", 500
    return "推送成功", 200
@app.route("/test/message",methods=["POST"])
# 测试环境方法
def test_dataProcess():
    if request.method =="POST":
        print(request.form)
        # template = "\n\n[![听云官网](https://saas.tingyun.com/static/website/images/ty-logo.png \"听云官网\")](https://www.tingyun.com \"听云官网\")\n\n**国内专业的应用性能监控平台**"
        content = str(request.form["content"])
        key = str(request.form["key"])
        name = str(request.form["name"])
        wx_url = str(request.form["wx_url"])
        res = utils(content,key,name,wx_url)
        return  res
    else:
        return "请求方法为POST",500
@app.route("/huadong/message",methods=["POST"])
# 生产环境方法
def product_dataProcess():
    if request.method =="POST":
        # print(request.form)
        # template ="\n\n[![听云官网](https://saas.tingyun.com/static/website/images/ty-logo.png \"听云官网\")](https://www.tingyun.com \"听云官网\")\n\n**国内专业的应用性能监控平台**"
        content = str(request.form["content"])
        key = str(request.form["key"])
        name = str(request.form["name"])
        wx_url = str(request.form["wx_url"])
        res = utils(content,key,name,wx_url)
        return  res
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 8089,
    debug=True
)
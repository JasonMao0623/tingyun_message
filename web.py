from flask import Flask,request
app =Flask(__name__)
import time
import log_out
import we_chat
def utils(mobiles_array,content):
    for mobile in mobiles_array:
        if content and mobile:
            we_chat.sendwx(content, "3288-cddd2195e76cfba892c071d7cfac279f")
            content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 短信发送成功 " + " 内容：" + \
                            request.form["content"] + " " + "接收人:" + " " + mobile
            log_out.log_out(content_value)
        else:
            content_value = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + " 短信发送失败 " + " 内容：" + \
                            request.form["content"] + " " + "接收人:" + " " + mobile
            log_out.log_out(content_value)
            return "推送失败请确认请求参数", 500
    return "推送成功", 200
@app.route("/test/message",methods=["POST"])
def dataprocess():
    if request.method =="POST":
        mobiles_array = request.form["mobile"].split(",")
        content = request.form["content"]
        res = utils(mobiles_array,content)
        return  res
    else:
        return "请求方法为POST",500
app.run(
    host="0.0.0.0",
    port = 8089,
    debug=True
)
from flask import Flask,request
app =Flask(__name__)
import time
import log_out
import we_chat
@app.route("/hycmcc/message",methods=["POST"])
def dataprocess():
    if request.method =="POST":
        mobiles_array = request.form["mobile"].split(",")
        content = request.form["content"]
        print(mobiles_array)
        for mobile in mobiles_array:
            if content and mobile:
                we_chat.sendwx(content)
                content_value=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" 短信发送成功 "+" 内容：" + request.form["content"]+" "+"接收人:"+" "+mobile
                log_out.log_out(content_value)
                # print(type(request.form["mobile"]))
                # print(json.dumps(res))
            else:
                content_value=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+" 短信发送失败 "+" 内容："+request.form["content"]+" "+"接收人:"+" "+mobile
                log_out.log_out(content_value)
                # print(type(request.form["mobile"]))
                return "短信发送失败",500
        return "短信发送成功",200
app.run(
    host="0.0.0.0",
    port = 53333,
    debug=True
)
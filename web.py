from flask import Flask,request
app =Flask(__name__)
import time
import log_out
import we_chat
import qiye_wexin
import process_data
def utils(content,sendkey,name,wx_url,Type):
    if content:
        if wx_url:
            qiye_wexin.send_message(content, wx_url,name)
        else:
            we_chat.sendwxnew(content,sendkey,name)
            we_chat.send(content,sendkey,name,Type)
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
        res = utils(content,key,name,"","平台告警")
        return  res
    else:
        return "请求方法为POST",500
@app.route("/huadong/qiyewx",methods=["POST"])
# 生产环境方法
def qiyewx():
    if request.method =="POST":
        # print(request.form)
        # template ="\n\n[![听云官网](https://saas.tingyun.com/static/website/images/ty-logo.png \"听云官网\")](https://www.tingyun.com \"听云官网\")\n\n**国内专业的应用性能监控平台**"
        content = str(request.form["content"])
        name = str(request.form["name"])
        key=""
        wx_url = str(request.form["wx_url"])
        res = utils(content,key,name,wx_url,"企业微信")
        return  res
    else:
        return "请求方法为POST",500
@app.route("/huadong/promethoes",methods=["POST"])
# 生产环境方法
def promethoes():
    test_data=b'{"receiver":"test","status":"firing","alerts":[{"status":"firing","labels":{"alertname":"\xe4\xb8\xbb\xe6\x9c\xba\xe8\xbf\x9c\xe7\xa8\x8b\xe8\xbf\x9e\xe6\x8e\xa5\xe5\xa4\xb1\xe8\xb4\xa5","host":"db-01","instance":"127.0.0.1:9066","job":"service_guard","service":"dbas"},"annotations":{"description":"db-01\xe4\xb8\xbb\xe6\x9c\xba\xe8\xbf\x9c\xe7\xa8\x8b\xe8\xbf\x9e\xe6\x8e\xa5\xe5\xa4\xb1\xe8\xb4\xa5.","summary":"db-01\xe4\xb8\xbb\xe6\x9c\xba\xe8\xbf\x9c\xe7\xa8\x8b\xe8\xbf\x9e\xe6\x8e\xa5\xe5\xa4\xb1\xe8\xb4\xa5."},"startsAt":"2019-04-03T16:22:20.137532326+08:00","endsAt":"0001-01-01T00:00:00Z","generatorURL":"http://mix-app-131-11:9090/graph?g0.expr=guard_remote_conn_up+%3D%3D+0\\u0026g0.tab=1"}],"groupLabels":{},"commonLabels":{"service":"dbas"},"commonAnnotations":{},"externalURL":"http://mix-app-131-11:9093","version":"4","groupKey":"{}:{}"}\n'
    print("========收到告警==========")
    # request.data = test_data
    processed_alerts = process_data.processData(request.data)
    for alert in processed_alerts:
        status=alert["status"]
        if status=="resolved":
            alarm="告警解除---"
        else:
            alarm="告警触发---"
        content_msg = alarm+alert["content"]
        key = alert["receiver"]
        alarmType=alarm+"自监控告警"
        print("告警消息为：" + content_msg)
        utils(content_msg,key,key,"",alarmType)
        # if res:
        #     log_out.log_out("告警:"+" 时间: "+alert["time"]+" 内容: "+ alert["content"])
        time.sleep(2)
    print("========告警已发送=========")
    return "告警成功"
@app.route("/health")
def health():
    return "green"
app.run(
    host="0.0.0.0",
    port = 8089,
    debug=True
)
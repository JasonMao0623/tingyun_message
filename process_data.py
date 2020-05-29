import json
import time
def processData(data):
    tmp_list=[]
    json_data = json.loads(data.decode())
    alerts = json_data["alerts"]
    status = json_data["status"]
    for alert in alerts:
        tmp_dict={}
        tmp_dict["status"]=status
        tmp_dict["content"]  = alert["annotations"]["description"]
        tmp_dict["receiver"] = json_data["receiver"]
        # tmp_dict["time"] = alert["startsAt"]
        tmp_dict["time"]=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        tmp_list.append(tmp_dict)
    return tmp_list


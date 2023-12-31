import requests
import time
import json
from urllib import request
import urllib

def get_access_token():
    corp_id = "" # 自行添加
    secret = “”  # 自行添加
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corp_id + "&corpsecret=" + secret
    req = urllib.request.Request(url)
    opener = urllib.request.build_opener()
    result = opener.open(req)
    json_data = json.loads(result.read().decode('utf-8'))
    return json_data['access_token']

def send_msg(agentid, msg, userid):
    data = '{"touser":"'+ userid +'","agentid":"'+ agentid +'","msgtype":"text","text":{"content":"'+ msg +'"}}'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+get_access_token()+'&debug=1'
    req = urllib.request.Request(url, data.encode('utf-8'))
    opener = urllib.request.build_opener()
    result = opener.open(req)
    return result.read().decode('utf-8')

# 请求的URL
url = "https://co2.cnki.net/Handler/Project.ashx?action=GetStuChoiceProjectsList"

# 请求体参数
data = {
    "isShowLoading": 0,
    "page": 1,
    "rows": 100,
    "authToken": "", # 自行添加
    "browserInfo": "",
    "dp": "xust"
}

# Cookie
# 自行添加
cookies = {
    "CO2017_AutoLoginId": "",
    "cur_role_id": "",
    "isEssenceVersion": "",
    "SID_checkdownload2": "",
    "CO2017_DomainPrefix": "",
    "login_usr_role": "",
    "ASP.NET_SessionId": "",
    "SID_co2": "",
    "Ecp_loginuserbk": "",
    "Ecp_session": "",
    "Ecp_ClientId": ""
}

while True:
    # 发送POST请求
    response = requests.post(url, data=data, cookies=cookies)
    
    # 解析返回的数据
    data = response.json()
    
    print(data)
    # 检查是否存在姓名为”123”的条目
    if any(item.get("姓名") == “#自行添加” for item in data.get("rows", [])):
        send_msg('#自行添加', ‘123题目已上线', '#自行添加')
        print("yes")
    else:
        print("no")
    
    # 每10分钟发送一次请求
    time.sleep(300)

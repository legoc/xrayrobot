from flask import Flask, request
import requests
import json
import time
app = Flask(__name__)
token="xxxxxxxxx"
headers = {'Content-Type': 'application/json;charset=utf-8'}
webhook="https://oapi.dingtalk.com/robot/send?access_token=%s"%(token)
def dingding_markdown_msg(webhook, message):
    time_local = time.localtime(message['create_time']/1000)
    stime = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    data_module = '''漏洞点: {url} \n\n漏洞模块: {plugin}\n\n出现时间: {datatime}'''.format(plugin=message['plugin'], url=message['target']['url'],datatime=stime)
    #print(data_module)
    json_text = {
        "msgtype": "markdown",
        "markdown": {
            "title":"xray warning",
            "text": data_module
        }
    }
    try:
        #print(json.dumps(json_text))
        info = requests.post(webhook, json.dumps(json_text), headers=headers).content
        #print(info)
    except Exception as e:
        print(str(e))
@app.route('/webhook', methods=['POST'])
def xray_webhook():
    try:
        dataall = request.json
        #print(dataall)
        data = dataall["data"]
        #print(data)
        #print("---1------")
        dingding_markdown_msg(webhook,data)
        #print("-----2----")
    except Exception as e:
        print(str(e))
    return 'ok'
if __name__ == '__main__':
    app.run(port=7071)
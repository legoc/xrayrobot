# xrayrobot
xray扫描结果推送到钉钉机器人



由于xray更新之后，推送到webhook的字段变了，以前搜到的不能用了。

参考这里改的：https://becivells.github.io/2019/12/xray_gaojing/

token处填上自己的机器人的token，

添加自定义机器人：https://www.dingtalk.com/qidian/help-detail-20781541.html

```
xray webscan --listen 0.0.0.0:7777 --html-output index.html --webhook-output http://127.0.0.1:7071/webhook
```


                                                                1.安装环境

依赖环境python3.10 (我用的是3.10 其他版本没测试)

操作系统  windows 、linux 都可以（企业微信需要对外提供服务，建议用linux),后面也可以编写dockefile 放容器内部跑

​                                                               2.安装依赖包

```
pip install -r requirements.txt
```

​                                                               3.程序发布

   程序打包压缩文件SparkAI_wechatcom.zip

   ![image-20231021105128615](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021105128615.png)

​    上传linux 服务器

​    ![image-20231021105245743](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021105245743.png)

​    解压程序包

​                  

```
unzip SparkAI_wechatcom.zip
```

​    windows 直接解压即可

   解压文件效果如下：

  windows 版本

   ![image-20231021105455391](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021105455391.png)               

linux 版本

![image-20231021105520758](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021105520758.png)

​                                                                   4.修改代码配置   

核心是修改config.json

```
{
  "WECHAT_TOKEN": "xxxx",
  "WECHAT_ENCODING_AES_KEY":"xxxx",
  "WECHAT_CORP_ID":"xxxx",
  "Secret":"xxxx",
  "AppId":"1000004",
  "xunfei_app_id":"xx",
  "xunfei_api_key":"xx",
  "xunfei_api_secret":"0dca3d2c79c0c243af6b96bb4f295dc3"
}

```

​      WECHAT_TOKEN、WECHAT_ENCODING_AES_KEY、WECHAT_CORP_ID、Secret、AppId 是企业微信里面的东西，需要修改成你的

​      xunfei_app_id、xunfei_api_key、xunfei_api_secret  是讯飞星火申请的API 需要的三个值，也需要换成你的

​                                                             5.程序运行

```
python  app.py
```

​     运行启动效果（Linux版本）

​    ![image-20231021111004052](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021111004052.png)

​     程序启动监听8888端口（如果需要修改端口，改wechatenterprise_channel.py 41行代码

```
    def startup(self):
        # start message listener
        app.run(host='0.0.0.0',port=8888)
```

​    linux 后台启动可以用nohup

```
  nohup python  app.py >/dev/null 2>&1 &
```

​     

   运行启动效果（windows版本）

  找到程序目录

![image-20231021111532138](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021111532138.png)

```
python app.py
```

![image-20231021111715840](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021111715840.png)

​                                                                                 6.企业微信配置

​     企业微信----应用管理---创建应用

​    ![image-20231021112157084](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112157084.png)

![image-20231021112222968](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112222968.png)

![image-20231021112449650](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112449650.png)

AgentId  和Secret 保存记录下来 分别对应上面conf.json 2个 值



![image-20231021112632519](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112632519.png)

接受消息 api这块需要设置

![image-20231021112730556](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112730556.png)

![image-20231021112840605](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021112840605.png)

URL  是你程序部署在外网的应用地址 我这里面地址是URLhttp://54.153.123.45:8888/wechat

 IP对应你公网IP (程序部署在内网，然后做防火墙映射也可以)    

8888 就是app.py启动监听的端口（也可以修改端口）

以上地址配置后微信需要验证这个地址是否通，通了才能使用。所以你程序部署好可以对外提供服务这个地方配置好就没有问题

Token 和EncodingAESKey  分别对应

需要设置conf.json 2个 值

![image-20231021113347264](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021113347264.png)

Token  对应上面WECHAT_TOKEN、EncodingAESKey   对应WECHAT_ENCODING_AES_KEY

WECHAT_CORP_ID 对应的地方如下图

![image-20231021130819321](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021130819321.png)

企业可信IP 

![image-20231021113511456](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021113511456.png)

 点击这个地方配置，因为企业微信对安全要求，这个地方类似防火墙白名单功能，只能运行在它白名单IP 服务器 才可以访问。

![image-20231021113647645](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231021113647645.png)

 配置效果如下，对外服务器如果是单服务器配置一个就可以了，如果多个按照；为风格，参考我上面的截图

```
117.68.158.58;124.220.204.108;36.7.87.66;54.153.123.45
```

​     我上面的是4个机器可以部署企业微信服务端，因为我有好几个公网服务器每次测试可以拿不通机器测试，这样提前配置我我就不需要折腾这块了。
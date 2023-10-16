# py_qzzdh

主要功能，启智平台自动登录，自动模拟人工智能云脑平台启动，容器内脚本自动化执行功能

# 先决条件
1. 拥有启智平台的登录账号，不会的小伙伴可以自行注册
2. 创建一个云脑容器平台
3. 云脑平台内部文件卷安装部署好frp linux版本软件 软件。
   frp_0.51.3_linux_amd64.tar.gz软下载地址（下载最新的软件包即可）
   https://github.com/fatedier/frp/releases
4. 需要一台公网服务器，这台服务器需要安装frp服务端，主要作用frp客户端反向链接到这个服务端使用

# 先决条件软件安装步骤

​     1.frp 服务端部署frps.ini （程序下载地址https://github.com/fatedier/frp/releases)

    [common]
    bind_port = 8000
    vhost_http_port =8000
    dashboard_port = 7500
    dashboard_user = admin
    dashboard_pwd =  admin

​    公网服务器 部署frp程序，其中选择服务端frps作为服务，启动监听8000端口，启动命令

```
nohup ./frps -c ./frps.ini >/dev/null 2>&1 &
```

   这里公网服务器需要对外开启8000端口，我用腾讯云给大家展示一下

   ![image-20231016234702694](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016234702694.png)

  测试验证frps 启动完成，我们可以通过管理端能够访问来证明

http://124.220.204.108:7500

![image-20231016234911243](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016234911243.png)

2. 启智平台创建代码及相关配置

   ![image-20231016235129239](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016235129239.png)

   

      迁移外部项目

   ![image-20231016235328785](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016235328785.png)

   ​    项目建立完成后如下图

   ![image-20231016235113186](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016235113186.png)

   

选择数据集---->关联数据集，输入我提供过数据集Qwen-7B-Chat-20231008

![image-20231016235827160](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016235827160.png)

![image-20231016235942189](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231016235942189.png)

点击云脑---》新建调试任务

![image-20231017000033931](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017000033931.png)

![image-20231017000127770](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017000127770.png)

​         基本信息 选择：智算网络集群，计算资源选择：英伟达GPU

​        参数设置：镜像：

```
192.168.242.22:443/default-workspace/fccb038c23234b9e80105d4ccd152117/image:cuda117_py310_pt2.0_langchain_chatglm
```

​    数据集选择我们刚才关联数据集

​    ![image-20231017000353944](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017000353944.png)

访问Interne：选择 是

资源规格：建议选择最贵的

 ![image-20231017000444089](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017000444089.png)

​             点击创建新任务 任务创建成功后我们可以看到再次就能看到如下画面

​            ![image-20231017000601124](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017000601124.png)

​             点击调试按钮 争取到资源，如果资源分配成功

​         

​            点击调试按钮进入 Jupyter Notebook 

   3. 启智平台启动 Jupyter Notebook 后相关配置

      

# 启智平台自动登录脚本说明

        Python安装在您的系统上
        python =">=3.7"
        请求库安装
        pip install selenium==4.8.0
        pip install loguru==0.7.0
        可以执行 pip install -r requirements.txt  一件执行
# windows 启动
        python main.py
# docker 镜像打包
        docker build -t pyqzzdh:v0.1 .
# docker 镜像运行
         docker run -d pyqzzdh:v0.1

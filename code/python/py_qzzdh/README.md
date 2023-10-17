# py_qzzdh

主要功能，启智平台自动登录，自动模拟人工智能云脑平台启动，容器内脚本自动化执行功能

# 先决条件
1. 拥有启智平台的登录账号，不会的小伙伴可以自行注册

   启智平台地址https://openi.pcl.ac.cn/

2. 创建一个云脑容器平台（后面详细介绍）

3. 云脑平台内部文件卷安装部署好frp linux版本软件 软件。
   frp_0.51.3_linux_amd64.tar.gz软下载地址（下载最新的软件包即可）
   https://github.com/fatedier/frp/releases
   
4. 需要一台公网服务器，这台服务器需要安装frp服务端，主要作用frp客户端反向链接到这个服务端使用

# 																		系统部署及原理图

![image-20231017132124658](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017132124658.png)

  1.启智平台提供容器计算服务，我们在容器计算服务内部部署通义千问大模型（Qwen-7B-Chat）和frp客户端程序。

2. 通过一个自动化监控爬虫程序监听启智平台提供容器计算服务实现触发启动命令及容器内部python组件包安装和通义千问大模型、frp客户端程序启动工作。
3. 启智平台提供容器计算服务提供4个小时的运行，运行完成后自动关闭。我们需要通过这个自动化程序监听容器是否对外提供服务，如果服务停止，里面自动实现重启。从而保证服务持续可用。



# 软件安装步骤

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

      ​     ![image-20231017111141707](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017111141707.png)

   程序启动后 代码是挂在 /code  目录下， 模型挂在 /dataset 目录下

  ![image-20231017112728022](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017112728022.png)

   进入 程序目录下 

![image-20231017112906880](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017112906880.png)

 输入 bash  、然后在输入 cd /code 进入代码目录下，默认情况下code 目录下只有一个master.zip 文件夹

![image-20231017113132117](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017113132117.png)

 我们需要解压程序master.zip，输入以下命令

```
unzip master.zip
```

 解压后就可以看到 qwen 文件夹了

![image-20231017113318400](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017113318400.png)

上传sh脚本到/code目录下

​     ![image-20231017111503527](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017111503527.png)

 sh脚本代码如下

```shell
# 进入目录
cd /code/qwen
# 安装依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
pip install auto-gptq optimum  -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn
pip uninstall langchain -y
pip install fastapi uvicorn openai "pydantic>=2.3.0" sse_starlette
# 启动frpc
cd frp_0.51.3_linux_amd64 && nohup ./frpc -c ./frpc.ini >/dev/null 2>&1&
# 启动Python应用程序
nohup python openai_api.py > log.txt&
echo "应用程序已启动."
```

   上传frp_0.51.3_linux_amd64.tar.gz到 /code/qwen 目录下

  ![image-20231017111742994](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017111742994.png)

 解压frp_0.51.3_linux_amd64.tar.gz

```
tar -xvf frp_0.51.3_linux_amd64.tar.gz
```

   ![image-20231017111902460](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017111902460.png)

 我们需要修改frpc.ini 文件 文件目录 cd /code/qwen/frp_0.51.3_linux_amd64 目录下

![image-20231017112033358](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017112033358.png)

配置文件如下：

```
[common]
server_addr = 124.220.204.108
server_port = 8000
   
[web]
type = http
local_port = 8000
custom_domains= 124.220.204.108

```

​    server_addr、server_port  是 公网服务器 IP  124.220.204.108  对应监听的端口8000

   web  配置简单说明

​     type = http   这个不需要修改

​     local_port  是本地 千问openai_api.py 代码中监听端口

​     ![image-20231017112448134](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017112448134.png)

   custom_domains  就换成远程服务器 IP ，当然你也可以换成远程服务器公网域名

接下来我们需要修改通义千问接口openai_api.py 代码，需要将模型地址修改成/dataset/Qwen-7B-Chat ，端口修改8000（这个根据情况选择，端口和相关配置要保持一致）

![image-20231017114027652](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017114027652.png)



注：如果dataset 模型没有自动解压，需要执行 解压命令 手工解压

```
unzip Qwen-7B-Chat.zip
```

![image-20231017113907828](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017113907828.png)

# 启智平台自动登录脚本说明

        Python安装在您的系统上
        python =">=3.7"
        请求库安装
        pip install selenium==4.8.0
        pip install loguru==0.7.0
        可以执行 pip install -r requirements.txt  一件执行
# windows 启动

​    修改代码 34、35行 代码，将34行无头模式代码注释，方便调试。35行代码geckodriver.exe 和代码文件目录结构保持一致

```
#option.add_argument('--headless')
driver = webdriver.Firefox(service=Service('D:\\devlop\\dev\\dazahui\\code\\python\\py_qzzdh\\util\\geckodriver.exe'), options=option)
```

​    使用火狐浏览器geckodriver.exe

​    ![image-20231017133742479](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017133742479.png)

    D:\develop\Python310\python.exe D:\develop\dazahui\code\python\py_qzzdh\main.py 
​    ![image-20231017134300239](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231017134300239.png)

​     运行程序后，程序会自动火狐浏览器运行起来。后面就完全自动化。

# docker 镜像打包

        docker build -t pyqzzdh:v0.1 .
# docker 镜像运行
         docker run -d pyqzzdh:v0.1

​     镜像运行和打包可以参考视频  video/启智平台docker镜像打包.mp4

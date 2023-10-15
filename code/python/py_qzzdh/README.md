# py_qzzdh

主要功能，启智平台自动登录，自动模拟人工智能云脑平台启动，容器内脚本自动化执行功能

# 先决条件
1. 拥有启智平台的登录账号，不会的小伙伴可以自行注册
2. 创建一个云脑容器平台
3. 云脑平台内部文件卷安装部署好frp linux版本软件 软件。
   frp_0.51.3_linux_amd64.tar.gz软下载地址（下载最新的软件包即可）
   https://github.com/fatedier/frp/releases
4. 需要一台公网服务器，这太服务器需要安装frp服务端，主要作用frp客户端反向链接到这个服务端使用

# 先决条件软件安装步骤
   





# 启智平台自动登录脚本说明
        Python安装在您的系统上
        python =">=3.7"
        请求库安装
        pip install selenium==4.8.0
        pip install loguru==0.7.0
        可以执行 pip install -r requirements.txt  一件执行
# windows 启动
        python main.py
# docker  启动
        docker run -it pyqzzdh:v0.1
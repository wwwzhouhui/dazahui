本项目主要是介绍googleapi使用
1. 安装环境
       python3.10
    
2.   安装库
       pip install -r  requirements.txt
    
3. 运行环境windows、linux 支持docker

4. 使用

     修改代码中google_search_key 、google_cx_id 为你自己的账号信息，申请地址可以参考https://zhuanlan.zhihu.com/p/174666017

    ![image-20231015081302835](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20231015081302835.png)

4. 运行
    
    python app.py
    
5. 部署docker
   docker build -t googleapi:v0.1 .
   
6. 运行docker
    docker run -d -p 6000:6000 googleapi:v0.1
    
8. 运行测试

    ![image-20231015080806888](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20231015080806888.png)

备注：由于googleapi 调用google建议使用国外服务器或则运行环境可以访问google 

FROM python:3.10-slim-buster

#定义环境变量
ENV TZ "Asia/Shanghai"
ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 安装 Firefox 和 geckodriver
RUN set -ex ;\
    apt update ;\
    apt install --no-install-recommends firefox-esr -y;\
    apt install wget -y ;\
    wget https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-linux64.tar.gz ;\
    tar -zxvf geckodriver-v0.33.0-linux64.tar.gz ;\
    rm geckodriver-v0.33.0-linux64.tar.gz ;\
    mv geckodriver /usr/local/bin ;\
    chmod +x /usr/local/bin/geckodriver ;\
    apt clean ;\
    apt autoclean ;\
    apt autoremove -y ;\
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/local/bin:${PATH}"

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn

COPY . .

CMD [ "python", "./main.py" ]

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
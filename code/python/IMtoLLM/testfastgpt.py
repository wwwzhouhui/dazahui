import requests
import json

url = "https://fastgpt.duckcloud.top/api/v1/chat/completions"
headers = {
    "Authorization": "Bearer fastgpt-AHFDo7pedzgsOUfimiuOxicP94Tj39KL3J-653cfad491788e21cca02053",
    "Content-Type": "application/json"
}
payload = {
    "chatId": "111",
    "stream": False,
    "detail": False,
    "variables": {
        "cTime": "2022/2/2 22:22"
    },
    "messages": [
        {
            "content": "CodeGeex国产免费自动代码生成助手，请告诉我们视频地址",
            "role": "user"
        }
    ]
}

response = requests.post(url, json=payload, headers=headers)
response_data = response.content.decode('utf-8')  # 读取响应内容
if response_data:
    response_json = json.loads(response_data)
    if "choices" in response_data and len(response_json["choices"]) > 0:
        content = response_json["choices"][0]["message"]["content"]
        print("Response Content:", content)
    else:
        print("No content found in the response.")

else:
    print("No response received.")
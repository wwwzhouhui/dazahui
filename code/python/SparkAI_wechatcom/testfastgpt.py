import requests

url = "http://192.168.1.9:23000/api/v1/chat/completions"
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
response_data = response.json()

if "choices" in response_data and len(response_data["choices"]) > 0:
    content = response_data["choices"][0]["message"]["content"]
    print("Response Content:", content)
else:
    print("No content found in the response.")

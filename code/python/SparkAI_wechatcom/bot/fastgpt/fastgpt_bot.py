# encoding:utf-8

import requests

from bot.bot import Bot
import time
from common.log import logger
from config import conf
#
class FastGPTBot(Bot):

    def __init__(self):
        super().__init__()
        self.fastgpt_url = conf().get("fastgpt_url")
        self.api_key = conf().get("fastgpt_api_key")

    def reply(self, query, context=None):
        t1 = time.time()
        url = self.fastgpt_url
        headers = {
            'Authorization': f'{self.api_key}',
            'Content-Type': 'application/json'
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
                    "content": f"{query}",
                    "role": "user"
                }
            ]
        }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        t2 = time.time()
        if "choices" in response_data and len(response_data["choices"]) > 0:
            content = response_data["choices"][0]["message"]["content"]
            logger.info(f"[reply] response={content}, time={t2 - t1}s")
            return content
        else:
            print("No content found in the response.")
            content = 'No content found in the response'
            logger.info(f"[reply] response={content}, time={t2 - t1}s")
            return content

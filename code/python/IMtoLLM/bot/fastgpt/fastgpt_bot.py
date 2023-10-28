# encoding:utf-8

import requests

from bot.session_manager import SessionManager
from bot.xunfei.wenxin_session import WenxinSession
from bot.bot import Bot
import time
from common.log import logger
from config import conf
import threading
import random
import queue
import json
# 消息队列 map
queue_map = dict()

# 响应队列 map
reply_map = dict()
#
class FastGPTBot(Bot):

    def __init__(self):
        super().__init__()
        self.fastgpt_url = conf().get("fastgpt_url")
        self.api_key = conf().get("fastgpt_api_key")
        # 和wenxin使用相同的session机制
        self.sessions = SessionManager(WenxinSession, model="fastgpt")

    def reply(self, query, context=None):
        logger.info("[fastgtp] query={}".format(query))
        session_id = context["from_user_id"]
        request_id = self.gen_request_id(session_id)
        logger.info("[fastgtp] session_id={}".format(session_id))
        logger.info("[fastgtp] request_id={}".format(request_id))
        reply_map[request_id] = ""
        session = self.sessions.session_query(query, session_id)
        threading.Thread(target=self.send_request, args=(session.messages, request_id)).start()
        depth = 0
        time.sleep(0.1)
        t1 = time.time()
        usage = {}
        while depth <= 300:
            try:
                data_queue = queue_map.get(request_id)
                if not data_queue:
                    depth += 1
                    time.sleep(0.1)
                    continue
                data_item = data_queue.get(block=True, timeout=0.1)
                if data_item.is_end:
                    # 请求结束
                    del queue_map[request_id]
                    if data_item.reply:
                        reply_map[request_id] += data_item.reply
                    usage = data_item.usage
                    break

                reply_map[request_id] += data_item.reply
                depth += 1
            except Exception as e:
                depth += 1
                continue
        t2 = time.time()
        logger.info(f"[fastgtp-API] response={reply_map[request_id]}, time={t2 - t1}s, usage={usage}")
        self.sessions.session_reply(reply_map[request_id], session_id, usage.get("total_tokens"))
        reply = reply_map[request_id]
        del reply_map[request_id]
        return reply

    def send_request(self, query,session_id):
        t1 = time.time()
        url = self.fastgpt_url
        data_queue = queue.Queue(1000)
        queue_map[session_id] = data_queue
        headers = {
            'Authorization': 'Bearer 'f'{self.api_key}',
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
        logger.info(f"[send_request] query={query}")
        logger.info(f"[send_request] fastgpt_url={url}")
        logger.info(f"[send_request] api_key={self.api_key}")
        logger.info(f"[send_request] headers={headers}")
        response = requests.post(url, json=payload, headers=headers,timeout=500)
        logger.info(f"[response] response={response}")
        response_data = response.content.decode('utf-8')  # 读取响应内容
        logger.info(f"[response.content] response_data={response_data}")
        t2 = time.time()
        if response_data:
            response_json = json.loads(response_data)
            data_queue = queue_map.get(session_id)
            if "choices" in response_json and len(response_json["choices"]) > 0:
                content = response_json["choices"][0]["message"]["content"]
                logger.info(f"[send_request] response={content}, time={t2 - t1}s")
                reply_item = ReplyItem(content,True)
                data_queue.put(reply_item)
                return content
            else:
                content = 'No content found in the response'
                logger.info(f"[send_request] response={content}, time={t2 - t1}s")
                reply_item = ReplyItem(content,True)
                data_queue.put(reply_item)
                return content
        else:
            content = 'No response received'
            logger.info(f"[send_request] response={content}, time={t2 - t1}s")
            reply_item = ReplyItem(content,True)
            data_queue.put(reply_item)
            return content

    def gen_request_id(self, session_id: str):
            return session_id + "_" + str(int(time.time())) + "" + str(random.randint(0, 100))

class ReplyItem:
    def __init__(self, reply, usage=None, is_end=False):
        self.is_end = is_end
        self.reply = reply
        self.usage = usage
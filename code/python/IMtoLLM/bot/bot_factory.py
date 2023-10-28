"""
channel factory
"""
from bot.xunfei.xunfei_spark_bot import XunFeiBot
from bot.fastgpt.fastgpt_bot import  FastGPTBot

def create_bot(bot_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """

    if bot_type == "xunfei":
        return XunFeiBot()
    elif bot_type == "fastgpt":
        return FastGPTBot()

    raise RuntimeError

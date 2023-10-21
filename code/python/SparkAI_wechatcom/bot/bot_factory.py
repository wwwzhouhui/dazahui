"""
channel factory
"""


def create_bot(bot_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """

    if bot_type == "xunfei":
        from bot.xunfei.xunfei_spark_bot import XunFeiBot
        return XunFeiBot()

    raise RuntimeError

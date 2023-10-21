import config
from common.log import logger
from channel import channel_factory
def run():
    try:
        # load config
        config.load_config()

        # create channel
        channel = channel_factory.create_channel("wxcom")   # 创建企业微信频道

        # startup channel
        channel.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)


if __name__ == "__main__":
    run()
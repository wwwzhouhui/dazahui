"""
channel factory
"""

from channel.wechatcom.wechatenterprise_channel import WechatEnterpriseChannel
def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    # if channel_type == 'wx':      # 创建微信频道
    #     return WechatChannel()
    if channel_type == 'wxcom':   # 创建企业微信频道
        return WechatEnterpriseChannel()
    # if channel_type == 'qq':      # 创建qq频道
    #     return QqchaChannel()
    # if channel_type == 'dd':      # 创建钉钉频道
    #     return DingTalkChannel()
    # if channel_type == 'feishu':  # 创建飞书频道
    #     return FeiShuChannel()
    # # if channel_type == 'telegram': # 创建电报频道
    # #     return TelegramChannel()
    # if channel_type == 'wxmp':     # 创建微信个人号
    #     return WechatSubsribeAccount()
    raise RuntimeError
class BaseDevConfig(object):
    # 测试开发时共有的一些配置...
    import os

    DEBUG = True
    SECRET_KEY = os.urandom(24)


class CMSDevConfig(BaseDevConfig):
    # 开发CMS系统时定制化的一些配置
    pass


class CMSProConfig(object):
    # CMS系统正式部署时根据自己的需要的一些配置,例如mysql配置，redis配置等等，
    pass

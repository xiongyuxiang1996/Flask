from flask import Flask
from .apis import apis as apis_blueprint
from .views import views as views_blueprint
from models import db
import config


def create_app():
    # 实例化实现了wsgi接口功能的flask对象
    app = Flask(__name__)
    # 增加app系统配置
    app.config.from_object(config)
    # 绑定数据库
    db.init_app(app)
    # 注册蓝图，并指定路由前缀
    app.register_blueprint(apis_blueprint, url_prefix='/apis')
    app.register_blueprint(views_blueprint, url_prefix='/views')
    return app

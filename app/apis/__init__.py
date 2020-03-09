from flask import Blueprint

# 实例化蓝图对象
apis = Blueprint("apis", __name__)

# 导入视图函数
from . import test1
from . import test2

from . import apis
from models import *
from modelsVO import *


@apis.route("/test1", methods=["GET"])
def test1():
    username = 'admin'
    user = User.query.filter(User.username == username).first()
    return UserVO(True, '500', None, user)

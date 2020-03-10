from . import apis
from models import *
from modelsVO import *


@apis.route("/test2", methods=["GET"])
def test2():
    username = 'admin'
    user = User.query.filter(User.username == username).first()
    return Result(True, '500', None, user.username)


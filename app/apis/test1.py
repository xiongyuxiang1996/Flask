from . import apis


@apis.route("/test1", methods=["GET"])
def test1():
     return "test1"

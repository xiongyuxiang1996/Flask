from . import apis


@apis.route("/test2", methods=["GET"])
def test2():
     return "test2"


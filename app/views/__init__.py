from flask import Blueprint, render_template

# 实例化蓝图对象
views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index_view():
    return render_template('index.html')

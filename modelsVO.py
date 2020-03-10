from flask import jsonify


def Result(success, code, msg, data):
    result = {
        'success': success,
        'code': code,
        'msg': msg,
        'data': data
    }
    return jsonify(result)


def UserVO(success, code, msg, user):
    data = {
        'id': user.id,
        'username': user.username,
        'password': user.password,
        'address': user.address
    }
    return Result(success, code, msg, data)

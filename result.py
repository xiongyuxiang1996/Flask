from flask import jsonify


def Result(success, code, msg, data):
    global dict
    # 如果date类型不是list
    if not isinstance(data, list):
        result = {
            'success': success,
            'code': code,
            'msg': msg,
            'data': data.getDict()
        }
    # 如果date类型是list
    else:
        datas = []
        for object in data:
            datas.append(object.getDict())
        result = {
            'success': success,
            'code': code,
            'msg': msg,
            'data': datas
        }
    return jsonify(result)


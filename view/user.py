import datetime
import hashlib
import json
import random
import string

from apistar import Response, http

from database import DB
from token import JWT


def user_auth(request: http.Request):
    '''
    :param request: JSONを渡す {"id": ID, "password": PASSWORD}
    :return: トークン
    '''
    try:
        user = json.loads(request.body)
    except:
        # JSON パースエラー
        return Response({"status": "err", "reason": "JSON Parse error"}, 403)

    db_data = DB.user.find_one({"id": user['id']})

    if not db_data:
        # データなし
        return Response({"status": "err", "reason": "user not found"}, 403)

    if not db_data['password'] == hashlib.sha256().update(db_data['salt'] + user['password']):
        return Response({"status": "err", "reason": "login failed"}, 403)

    return JWT.encode({"id": user['id'], "email": user['email'], "name": user['name']
                       })


def user_join(request: http.Request):
    '''
    :param request:  JSONを渡す {"id": ID, "password": PASSWORD, "email": EMAIL}
    :return: トークン
    '''

    try:
        user = json.loads(request.body)
    except:
        # JSON パースエラー
        return Response({"status": "err", "reason": "JSON Parse error"}, 403)

    # ここでは当該IDのデータが存在「してはならない」
    if DB.user.find_one({"id": user['id']}):
        # データ「あり」
        return Response({"status": "err", "reason": "user not found"}, 403)

    salt = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(32)])

    DB.user.insert_one({
        "id": user   ['id'],
        "email": user['email'],
        "name": user ['name'],
        "join_at":   datetime.datetime.now(),
        "password":  hashlib.sha256().update(salt + user['password']),
        "salt":      salt
    })

    return JWT.encode({"id": user['id'], "name": user['name']})

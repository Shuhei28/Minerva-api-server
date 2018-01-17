from token import JWT


def auth_check(authorization):
    '''
    :param authorization:
    :return:
    '''
    try:
        # Authorizationヘッダのパース
        authorization_body = authorization.split(" ")

        # Authorizationヘッダの先頭がBearerかどうかのチェック
        if authorization_body[0] != "Bearer":
            return False

        # Authorizationヘッダからトークンの抽出
        token = authorization_body[1]

        # JWTのデコード
        obj = JWT.decode(token)
        if obj is None:
            return False
    except:
        return False

    # IDのみを返す
    return obj.get("id")

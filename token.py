import json

import jwt as jwtlib


class JWT:
    key = "M1NERV@"

    @staticmethod
    def encode(obj):
        if isinstance(obj, (dict, list)):
            obj = json.dumps(obj)
        return jwtlib.encode(obj, key=JWT.key, algorithm='HS256')

    @staticmethod
    def decode(obj):
        if isinstance(obj, bytes):
            obj = obj.decode("utf-8")
        if isinstance(obj, int):
            obj = str(obj)
        return jwtlib.decode(obj, key=JWT.key, algorithm='HS256', verify=False)

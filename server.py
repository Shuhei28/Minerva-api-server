from apistar import Route
from apistar.frameworks.wsgi import WSGIApp as App

from view.user import user_auth, user_join


def ping():
    '''
    :return: dict
    '''
    return {"status": "ok"}


routes = [Route('/ping', 'GET', ping),

    # 認証
    Route('/user/auth', "GET", user_auth), Route('/user/join', "POST", user_join)

]

app = App(routes=routes)  # Install custom components.)

if __name__ == "__main__":
    app.main(["run"])

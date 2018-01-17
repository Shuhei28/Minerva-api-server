from apistar import Response, http

from database import DB
from view.auth import auth_check


# クエスチョン全問取得
def questions_get(request: http.Request):
    '''
    :return Response: 全問題の概要のみを返す
    '''
    return Response([{"id": str(question['_id']), "title": question['title'], 'description': question['description']
    } for question in DB.questions.find()], 200)


# クエスチョン１問取得
def question_get(question_id, request: http.Request):
    '''
    :param question_id:
    :return Response: 1問のデータを全て返す
    '''
    if not auth_check(request.headers.get("Authorization")):
        return Response({"status": 'error', 'reason': 'not authorized'}, 400)

    try:
        question = DB.questions.find_one({"id": question_id})
    except:
        return Response({"status": 'error', 'reason': 'not found'}, 404)

    return Response({
                        "id":                  str(question['_id']),
                        "title": question      ['title'],
                        'description': question['description'],
                        'questions': question  ['question']
                        }, 200)


# クエスチョン投稿
def questions_post(request: http.Request):
    '''
    :param request: JSON
    :return: 成功かどうかのステータスを返す
    '''
    # 型
    {

    }
    if not auth_check(request.headers.get("Authorization")):
        return Response({"status": 'error', 'reason': 'not authorized'}, 400)

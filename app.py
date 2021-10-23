from flask import Flask, request

from server.requset_processors import process_request


app = Flask(__name__)


@app.route("/api/get_user", methods=['GET'])
def get_user():
    """Получение информации о пользователе"""

    return process_request('get_user', request.get_json(force=True))


@app.route('/')
def base_check():
    """Для проверки активности сервера"""
    return '.'


if __name__ == '__main__':
    app.run()

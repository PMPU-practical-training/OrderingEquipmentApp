from flask import request
from flask_login import login_required

from server.requset_processors import process_request
from globals import *


@app.route("/api/get_user", methods=['GET'])
@login_required
def get_user():
    """Получение информации о пользователе"""

    return process_request('get_user', request.get_json(force=True))


@app.route('/')
def base_check():
    """Для проверки активности сервера"""
    return '.'


if __name__ == '__main__':
    app.run()

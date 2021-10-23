def get_user(handler, data):
    user = handler.get_user(data['user_id'])
    return {
        'user_id': user.id,
    }

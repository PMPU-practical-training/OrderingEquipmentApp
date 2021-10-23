import logging
import functools

from sqlalchemy.orm import sessionmaker, scoped_session
from database.__main__ import engine, Base

import database.models.user as user_model
import database.exceptions.exceptions as database_exceptions


logger = logging.getLogger(__name__)


def with_session_commit(func):
    """Использовать этот декоратор с методами DBHandler, в который изменяются данные в базе"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args[0].db_session.commit()
        return result
    return wrapper


class DBHandler:
    def __init__(self):
        logger.info('Init DBHandler')

        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
        Base.query = self.db_session.query_property()

    def __enter__(self):
        self.__init__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db_session.remove()

    def remove_session(self):
        self.db_session.remove()

    def get_user(self, user_id):
        filter_condition = (user_model.User.user_id == user_id)
        user = user_model.User.query.filter(filter_condition).first()

        if not user:
            raise database_exceptions.ItemNotFountError('There is not user with id={}'.format(user_id))
        return user

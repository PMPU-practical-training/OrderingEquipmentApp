from sqlalchemy import Column, Integer
from database.__main__ import Base


class User(Base):
    """
    Пользователи
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))
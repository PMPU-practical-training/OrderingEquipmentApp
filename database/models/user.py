from sqlalchemy import Column, Integer, false
from database.__main__ import Base


class User(Base):
    """
    Пользователи
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(Integer,nullable=false)
    passw = Column(Integer,nullable=false)
    name = Column(Integer,nullable=false)
    role = Column(Integer,nullable=false)

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(
            ['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

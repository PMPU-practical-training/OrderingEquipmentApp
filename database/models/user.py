from sqlalchemy import Column, Integer, false, String
from database.__main__ import Base


class User(Base):
    """
    Пользователи
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String,nullable=false)
    passw = Column(String,nullable=false)
    name = Column(String,nullable=false)
    role = Column(String,nullable=false)

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(
            ['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

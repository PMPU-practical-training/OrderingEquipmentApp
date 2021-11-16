from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from database.__main__ import Base
from sqlalchemy.orm import relationship

class User(Base, UserMixin):
    """
    Пользователи
    """

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    passw = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    role = Column(String, nullable=False)
    Order = relationship("Order")

    def set_password(self, passw):
        self.password_hash = generate_password_hash(passw)

    def check_password(self, passw):
        return check_password_hash(self.password_hash, passw)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))
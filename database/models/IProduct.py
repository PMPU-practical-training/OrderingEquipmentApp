from werkzeug.security import generate_password_hash,  check_password_hash

from sqlalchemy import Column, Integer, String, Boolean
from database.__main__ import Base


class Product(Base):
    """
    Пользователи
    """

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    verifiedBy = Column(String, nullable=False)
    requiresVerefication = Column(Boolean(), primary_key=True)
    price = Column(Integer, nullable=True)




    def get_id(self):
        return self.Product_id

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))
from sqlalchemy import Column, Integer, Text, Boolean
from database.__main__ import Base


class Product(Base):
    """
    Продукты
    """

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    verified_by = Column(Text)
    requires_verification = Column(Boolean)
    price = Column(Float, nullable=True)

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

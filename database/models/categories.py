from sqlalchemy import Column, Integer, String, ForeignKey
from database.__main__ import Base
from sqlalchemy.orm import relationship

class categories(Base):
    """
    Продукты
    """

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    subcategory_id = Column(Integer, ForeignKey('subcategory_id'))

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

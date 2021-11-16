from sqlalchemy import Column, Integer, Text, String
from database.__main__ import Base


class Specifications(Base):
    """
    Продукты
    """

    __tablename__ = "Specifications"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    type = Column(String)
    subcategory_id = Column(Integer, default=None)

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

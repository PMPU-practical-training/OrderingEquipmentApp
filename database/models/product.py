from sqlalchemy import Column, Integer, Text, Boolean, Float, ForeignKey
from database.__main__ import Base
from sqlalchemy.orm import relationship

class Product(Base):
    """
    Продукты
    """

    __tablename__ = "product"
    children = relationship("Child")
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    verified_by = Column(Text, default=None)
    requires_verification = Column(Boolean, default=False)
    price = Column(Float, nullable=True)
    subcategory_id = Column(Integer, default=None)
    categories = relationship("category")

    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

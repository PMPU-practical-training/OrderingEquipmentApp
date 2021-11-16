from sqlalchemy import Column, Integer, Text, String, ForeignKey
from database.__main__ import Base
from sqlalchemy.orm import relationship

class Order(Base):
    """
    Продукты
    """

    __tablename__ = "Order"

    doc_link = Column(String, nullable=False, unique=True)
    app_id = Column(Integer, primary_key=True)
    req_number = Column(String)
    req_dates = Column(String)
    req_name = Column(String)
    req_address = Column(String)
    req_finance = Column(String)
    req_contract = Column(String)
    req_responsible = Column(String)
    user_id = Column(Integer, ForeignKey('user_id'))



    def __repr__(self):
        return "{}: {}".format(self.__name__, ', '.join(['{}={}'.format(key, value) for key, value in self.__dict__ if not key.startswith('__')]))

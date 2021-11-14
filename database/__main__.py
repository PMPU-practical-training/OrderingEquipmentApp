from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

import os

engine = create_engine(os.environ.get('DATABASE_URL'), convert_unicode=True)
Base = declarative_base()


def init_db():
    """При каждом изменении структуры БД следует из консоли heroku запускать эту функцию
    Не забывайте сюда импортировать все модели!
    """

    from database.models import user
    from database.models import product
    Base.metadata.create_all(bind=engine)

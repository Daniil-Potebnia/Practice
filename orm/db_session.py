from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from db_config import settings

SqlBase = declarative_base()
__factory = None


def global_init():
    global __factory

    engine = create_engine(settings.db_url_psycopg, echo=False)
    __factory = sessionmaker(bind=engine)

    from . import __all_models

    SqlBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()

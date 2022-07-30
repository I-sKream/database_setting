"""
This is SQLAlchemy context manager!
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_setting import url_setting


DATABASE_PATH = url_setting["database_url"]


class SqlAlchemyContextManager:
    """
    """
    def __init__(self):

        engine = create_engine(DATABASE_PATH, echo=True, future=True)

        Session = sessionmaker(engine)
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
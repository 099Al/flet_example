import os

from sqlalchemy import create_engine, Table, MetaData, select
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


class Database:
    def __init__(self):
        load_dotenv()
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.connect = 'sqlite:///D:/WorkSpaces/PythonWs/shop/db.sqlite3'
        #self.connect =  f'postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}'
        self.engine = create_engine(self.connect)
        self.metadata = MetaData()
        self.Base = declarative_base()

        self.adminUser = Table('logins', self.metadata, autoload_with=self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def check_email(self, email):
        result = self.session.execute(
            select(self.adminUser)
            .where(self.adminUser.c.email == email)
        )
        return result.fetchone()




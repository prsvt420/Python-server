from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from settings import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    password = Column(String(128))

    def __repr__(self):
        return f'User - {self.username}'


if __name__ == '__main__':
    Base.metadata.create_all(engine)

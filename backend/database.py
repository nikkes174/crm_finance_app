from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# подключение в бд
DATABASE_URL = "postgresql://postgres:1488Zigazaga@localhost:5432/finance"

# движок для поюключения к БД, для управления SQL-запросами
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# создаём базовый класс
Base = declarative_base()
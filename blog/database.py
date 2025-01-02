#Import statements
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#URL CONNECTIVITY
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

#START ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

#CREATE SESSION
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#DECLARE MAPPING
Base = declarative_base()

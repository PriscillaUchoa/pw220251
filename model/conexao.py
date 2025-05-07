from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATA_BASE_URL = 'sqlite:///./banco.db'
engine = create_engine(DATA_BASE_URL, echo=True)
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the engie 
engine = create_engine("sqlite:///todo.db")

Base = declarative_base()

# create the sesion 
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


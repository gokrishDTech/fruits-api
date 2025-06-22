from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

# DB model for SQLAlchemy
class FruitDB(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, index=True)
    fruit = Column(String)
    color = Column(String)

# Pydantic model for POST request body validation
class FruitCreate(BaseModel):
    fruit: str
    color: str

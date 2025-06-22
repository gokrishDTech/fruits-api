from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import os

# Use test.db if TESTING=1 is set in env
USE_TEST_DB = os.getenv("TESTING", "0") == "1"
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" if USE_TEST_DB else "sqlite:///./fruits.db"

# Set up SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables if not already created
Base.metadata.create_all(bind=engine)

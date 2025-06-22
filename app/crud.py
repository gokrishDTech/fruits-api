from fastapi import HTTPException
from app.models import FruitDB, FruitCreate
from sqlalchemy.orm import Session

# Add a new fruit to the DB
def create_fruit(db: Session, fruit: FruitCreate):
    existing = db.query(FruitDB).filter(FruitDB.fruit == fruit.fruit).first()
    if existing:
        raise HTTPException(status_code=400, detail="Fruit already exists")
    db_fruit = FruitDB(**fruit.model_dump())
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

# Get one fruit by ID
def get_fruit_by_id(db: Session, fruit_id: int):
    return db.query(FruitDB).filter(FruitDB.id == fruit_id).first()

# Get all fruits
def get_all_fruits(db: Session):
    return db.query(FruitDB).all()

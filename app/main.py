from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, models

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/fruits")
def read_fruits(db: Session = Depends(get_db)):
    return crud.get_all_fruits(db)

@app.get("/fruits/{fruit_id}")
def read_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = crud.get_fruit_by_id(db, fruit_id)
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit

@app.post("/fruits")
def create_fruit(fruit: models.FruitCreate, db: Session = Depends(get_db)):
    return crud.create_fruit(db, fruit)

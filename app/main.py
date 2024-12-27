from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

app = FastAPI()

# Инициализация базы данных
database.init_db()

# Зависимость для получения сессии
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Получение списка всех терминов
@app.get("/terms/", response_model=list[schemas.TermInDB])
def get_terms(db: Session = Depends(get_db)):
    terms = db.query(models.Term).all()
    return terms

# Получение информации о конкретном термине
@app.get("/terms/{term_name}", response_model=schemas.TermInDB)
def get_term(term_name: str, db: Session = Depends(get_db)):
    term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    return term

# Добавление нового термина
@app.post("/terms/", response_model=schemas.TermInDB)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    db_term = models.Term(term=term.term, description=term.description)
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term

# Обновление существующего термина
@app.put("/terms/{term_name}", response_model=schemas.TermInDB)
def update_term(term_name: str, term: schemas.TermUpdate, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db_term.description = term.description
    db.commit()
    db.refresh(db_term)
    return db_term

# Удаление термина
@app.delete("/terms/{term_name}")
def delete_term(term_name: str, db: Session = Depends(get_db)):
    db_term = db.query(models.Term).filter(models.Term.term == term_name).first()
    if db_term is None:
        raise HTTPException(status_code=404, detail="Term not found")
    db.delete(db_term)
    db.commit()
    return {"message": "Term deleted successfully"}

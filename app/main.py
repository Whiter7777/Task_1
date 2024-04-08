from db.database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse

Base.metadata.create_all(bind=engine)
app = FastAPI()
some_file_path = "index.html"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return FileResponse("public/index.html")

@app.get("/payment_methods")
def get_people(db: Session = Depends(get_db)):
    return db.query(Payment_method).all()

@app.post("/payment_methods")
def create_payment_method(data = Body(), db: Session = Depends(get_db)):
    payment_method = Payment_method(name = data["name"], logo = data["logo"], short_name = data["short_name"], description = data["description"])
    db.add(payment_method)
    db.commit()
    db.refresh(payment_method)
    return payment_method

@app.delete("/payment_methods/{id}")
def delete_payment_method(id, db: Session = Depends(get_db)):
    payment_method = db.query(Payment_method).filter(Payment_method.id == id).first()
    if payment_method == None:
        return JSONResponse (status_code=404, content={ "message": "Платежная система не найдена"})
    db.delete(payment_method)
    db.commit()
    return payment_method




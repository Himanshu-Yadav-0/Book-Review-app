from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from typing import List

router = APIRouter(tags=["Reviews"])

@router.get("/books/{book_id}/reviews", response_model=List[schemas.ReviewOut])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_for_book(book_id, db)

@router.post("/books/{book_id}/reviews", response_model=schemas.ReviewOut)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.add_review_to_book(book_id, review, db)

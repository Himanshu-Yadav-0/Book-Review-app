from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
from typing import List

router = APIRouter(prefix="/v1", tags=["Reviews"])

@router.get("/books/{book_id}/reviews", response_model=List[schemas.ReviewOut], status_code=status.HTTP_200_OK)
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    # Check if book exists
    book = crud.get_book_by_id(book_id, db)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return crud.get_reviews_for_book(book_id, db)

@router.post("/books/{book_id}/reviews", response_model=schemas.ReviewOut, status_code=status.HTTP_201_CREATED)
def add_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    # Check if book exists
    book = crud.get_book_by_id(book_id, db)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    
    try:
        return crud.add_review_to_book(book_id, review, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating review: {str(e)}"
        )

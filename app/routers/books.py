from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app import schemas, crud
from app.database import get_db
from typing import List
from app.cache import get_cache, set_cache


router = APIRouter(prefix="/v1/books", tags=["Books"])


@router.get("/", response_model=List[schemas.BookOut], status_code=status.HTTP_200_OK)
def list_books(db: Session = Depends(get_db)):
    cache_key = "books:all"
    try:
        cached = get_cache(cache_key)
        if cached:
            print("✅ Redis Cache HIT")
            return cached
        print("❌ Redis Cache MISS")
    except Exception as e:
        print(f"⚠️ Redis error: {str(e)} (continuing with DB...)")

    books = crud.get_all_books(db)

    try:
        serialized_books = jsonable_encoder(books)
        set_cache(cache_key, serialized_books, ttl=60)
        print("✅ Redis Cache SET")
    except Exception as e:
        print(f"⚠️ Redis error during set: {str(e)}")

    return books


@router.post("/", response_model=schemas.BookOut, status_code=status.HTTP_201_CREATED)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_book(book, db)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating book: {str(e)}"
        )

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from app import schemas, crud
from app.database import get_db
from typing import List
from app.cache import get_cache, set_cache


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[schemas.BookOut])
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


@router.post("/", response_model=schemas.BookOut)
def add_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(book, db)

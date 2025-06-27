from sqlalchemy.orm import Session
from app import models, schemas
from app.cache import delete_cache

def get_all_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(book_id: int, db: Session):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def create_book(book: schemas.BookCreate, db: Session):
    new_book = models.Book(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)    
    delete_cache("books:all")
    return new_book

def get_reviews_for_book(book_id: int, db: Session):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()

def add_review_to_book(book_id: int, review: schemas.ReviewCreate, db: Session):
    new_review = models.Review(book_id=book_id, content=review.content, rating=review.rating)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

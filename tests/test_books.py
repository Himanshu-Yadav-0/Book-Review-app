import json
from fastapi.testclient import TestClient
from app.main import app
import redis

client = TestClient(app)

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def clear_cache():
    redis_client.flushdb()


def test_get_books_cache_miss(monkeypatch):
    """
    Integration test: Cache MISS flow.
    """
    clear_cache()  

    response = client.get("/v1/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_book():
    """
    Unit test for POST /v1/books/ endpoint
    """
    payload = {
        "title": "Test Driven Dev",
        "author": "Kent Beck"
    }
    response = client.post("/v1/books/", json=payload)
    assert response.status_code == 201 
    data = response.json()
    assert data["title"] == "Test Driven Dev"
    assert data["author"] == "Kent Beck"


def test_add_review():
    """
    Unit test for POST /v1/books/{book_id}/reviews endpoint
    """
    book_id = 1
    review_payload = {
        "rating": 5,
        "content": "Excellent book! Really helped me understand TDD concepts."
    }
    response = client.post(f"/v1/books/{book_id}/reviews", json=review_payload)
    assert response.status_code == 201 
    data = response.json()
    assert data["rating"] == 5
    assert data["content"] == "Excellent book! Really helped me understand TDD concepts."



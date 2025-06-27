# Book Review API

A modern FastAPI-based Book Review system with Redis caching, PostgreSQL database, and comprehensive testing suite.

## 🚀 Features

- **RESTful API** for managing books and reviews
- **Redis Caching** for improved performance
- **PostgreSQL Database** with SQLAlchemy ORM
- **Database Migrations** with Alembic
- **Comprehensive Testing** with Pytest
- **Input Validation** with Pydantic
- **Docker Support** for easy deployment

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose (recommended)

## 🛠 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd book-review-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL
REDIS_URL
```

### 5. Start External Services

#### Using Docker Compose (Recommended)

```bash
# Start Redis
docker-compose up -d
```

#### Manual Setup

**PostgreSQL:**
- Install PostgreSQL
- Create database: `createdb book`
- Update DATABASE_URL in `.env` with your credentials


## 🗄️ Database Migrations

### Run Initial Migration

```bash
# Initialize Alembic (only needed once)
alembic upgrade head
```

### Create New Migration (when models change)

```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

### Migration Commands

```bash
# Check current migration version
alembic current

# View migration history
alembic history

# Downgrade to previous migration
alembic downgrade -1
```

## 🚀 Running the Service

### Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL:** `http://localhost:8000`
- **Interactive Docs:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_books.py
```

### Test Categories

- **Unit Tests:** Test individual endpoints and functions
- **Integration Tests:** Test Redis caching and database interactions

## 📚 API Documentation

### Books Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books (cached) |
| POST | `/books/` | Create a new book |

### Reviews Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/{book_id}/reviews` | Get reviews for a book |
| POST | `/books/{book_id}/reviews` | Add review to a book |

### Example API Calls

#### Create a Book

```bash
curl -X POST "http://localhost:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Clean Code",
    "author": "Robert C. Martin"
  }'
```

#### Add a Review

```bash
curl -X POST "http://localhost:8000/books/1/reviews" \
  -H "Content-Type: application/json" \
  -d '{
    "rating": 5,
    "content": "Excellent book for software developers!"
  }'
```

#### Get All Books

```bash
curl -X GET "http://localhost:8000/books/"
```

## 🏗 Project Structure

```
book-review-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── cache.py             # Redis caching utilities
│   └── routers/
│       ├── books.py         # Books API endpoints
│       └── reviews.py       # Reviews API endpoints
├── tests/
│   └── test_books.py        # Test cases
├── alembic/                 # Database migration files
├── requirements.txt         # Python dependencies
├── docker-compose.yml       # Docker services configuration
├── alembic.ini             # Alembic configuration
├── .env                    # Environment variables
└── README.md               # This file
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `REDIS_URL` | Redis connection string | Required |

### Cache Configuration

- **Cache TTL:** 60 seconds for book listings
- **Cache Key Pattern:** `books:all`
- **Cache Behavior:** Cache miss falls back to database

## 🔧 Development

### Adding New Endpoints

1. Define Pydantic schemas in `app/schemas.py`
2. Create database models in `app/models.py`
3. Add CRUD operations in `app/crud.py`
4. Create router endpoints in `app/routers/`
5. Include router in `app/main.py`
6. Write tests in `tests/`

### Database Model Changes

1. Update models in `app/models.py`
2. Generate migration: `alembic revision --autogenerate -m "description"`
3. Review and edit migration file if needed
4. Apply migration: `alembic upgrade head`

### Performance Monitoring

- Monitor Redis cache hit/miss rates in application logs
- Check database query performance
- Monitor API response times

## 📝 Notes

- The application uses Redis for caching book listings to improve performance
- All API inputs are validated using Pydantic schemas
- Database operations use SQLAlchemy ORM for type safety
- Tests cover both unit and integration scenarios
- Migrations are managed through Alembic for safe database updates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with tests
4. Run test suite
5. Submit a pull request

---

**Built with ❤️ using FastAPI, PostgreSQL, and Redis by Himanshu Yadav**

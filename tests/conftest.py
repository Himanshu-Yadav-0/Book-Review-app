import pytest
from fastapi.testclient import TestClient
from app.main import app  # make sure app is imported from the correct file

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def db():
    # Just a dummy placeholder if not needed inside test
    return None

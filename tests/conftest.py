from main import app
from unittest.mock import MagicMock
from db_setup import get_session
import pytest


mock_session = MagicMock()

def override_get_db():
    try:
        yield mock_session
    finally:
        pass


app.dependency_overrides[get_session] = override_get_db

@pytest.fixture
def mock_db_session():
    return mock_session
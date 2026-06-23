import pytest
from app.schemas import UserCreate


def test_user_create_schema():
    user_data = {'email': 'test@example.com', 'password': 'securepassword'}
    user = UserCreate(**user_data)
    assert user.email == 'test@example.com'
    assert user.password == 'securepassword'
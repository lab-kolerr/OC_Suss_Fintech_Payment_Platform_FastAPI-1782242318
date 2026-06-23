import pytest

@pytest.fixture(scope='session')
def db_session():
    # Setup database session
    yield
    # Teardown database session
import pytest
from mockito import unstub

@pytest.fixture
def unstub_user():
    yield unstub()
from datetime import datetime
# from tut07_fixture_factory.main_app.app import Student
from tut07_fixture_factory.main_app.app import Student
import pytest


@pytest.fixture
def dummy_student():
    return Student("Prabhat",datetime(2000,1,1),"coe",50)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name,credits):
        return Student(name,datetime(2000,1,1),"coe",credits)
    return _make_dummy_student
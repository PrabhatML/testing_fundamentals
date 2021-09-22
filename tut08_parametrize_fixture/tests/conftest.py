from datetime import datetime
from tut08_parametrize_fixture.main_app.app import Student
import pytest


@pytest.fixture
def dummy_student(request):
    if getattr(request,'param',None):
        return Student("Prabhat",datetime(2000,1,1),"coe",request.param)
    return Student("Prabhat",datetime(2000,1,1),"coe",50)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name,credits):
        return Student(name,datetime(2000,1,1),"coe",credits)
    return _make_dummy_student
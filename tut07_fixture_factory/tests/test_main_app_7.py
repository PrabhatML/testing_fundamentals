from datetime import datetime
from tut07_fixture_factory.main_app.app import get_topper

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days//365
    assert dummy_student_age == dummy_student.get_age()


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 50


def test_get_topper(make_dummy_student):
    students = [
        make_dummy_student("ram",21),
        make_dummy_student("shyam",19),
        make_dummy_student("ravi",25)
    ]
    topper = get_topper(students)
    assert topper == students[2]
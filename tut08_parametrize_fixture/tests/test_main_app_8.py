from datetime import datetime
from tut08_parametrize_fixture.main_app.app import is_eligible_for_degree
import pytest

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days//365
    assert dummy_student_age == dummy_student.get_age()

def test_student_is_eligibile_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("Sam",19)) == False

def test_student_is_eligibile_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("Sam",21)) == True

# With fixture factory
@pytest.mark.parametrize(argnames="credits,expected",argvalues=[(19,False),(21,True)])
def test_student_is_eligibile_for_degree(make_dummy_student,credits,expected):
    assert is_eligible_for_degree(make_dummy_student("Sam",credits)) == expected

# Without fixture factory -> Using direct object
@pytest.mark.parametrize(argnames="dummy_student,expected",argvalues=[(19,False),(21,True)],
                        indirect=["dummy_student"],ids=["ineligible","eligible"])
def test_student_is_eligibile_for_degree_using_object(dummy_student,expected):
    assert is_eligible_for_degree(dummy_student) == expected


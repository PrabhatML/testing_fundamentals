from tut02_excpetion_test.main_app.app import validate_age
import pytest

def test_validate_age_valid_age():
    assert validate_age(10) == "Correct"

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)
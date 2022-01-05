from tut03_mark_skip.main_app.app import sample_add
import pytest
import sys

class TestSample:
    @pytest.mark.skip(reason="Just wanna skip")
    def test_sample_add_number(self):
        assert sample_add(1,2) == 3

    @pytest.mark.skipif(sys.version_info>(3,7),reason="Skip if python version is more than 3.7")
    def test_sample_add_str(self):
        assert sample_add("a","b") == "ab"

    # When user is ok with failed test cases
    @pytest.mark.xfail(sys.platform == "win32",reason="Dont run on windows")
    def test_sample_add_number(self):
            assert sample_add(1,2) == 3
            raise Exception()

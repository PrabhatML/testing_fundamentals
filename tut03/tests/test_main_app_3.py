from tut03.main_app.app import sample_add
import pytest
import sys

class TestSample:
    @pytest.mark.skip(reason="Just wanna skip")
    def test_sample_add_number(self):
        assert sample_add(1,2) == 3

    @pytest.mark.skipif(sys.version_info>(3,7),reason="Skip if python version is more than 3.7")
    def test_sample_add_str(self):
        assert sample_add("a","b") == "ab"

    @pytest.mark.xfail
    def test_sample_add_number(self):
            assert sample_add(1,2) == 3
            raise Exception()

from tut01.sample_functions.func import sample_add


class TestSample:
    def test_sample_add_number(self):
        assert sample_add(1,2) == 3


    def test_sample_add_str(self):
        assert sample_add("a","b") == "ab"

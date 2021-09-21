from tut04.main_app.app import sample_add
import pytest

class TestSample:
    
    def test_add_num(self):
        assert sample_add(1,2) == 3

    def test_str_num(self):
        assert sample_add("a","b") == "ab"

    def test_lst_num(self):
        assert sample_add([1,2],[3]) == [1,2,3]

    @pytest.mark.parametrize(argnames="x,y,z",
                            argvalues=[(1,2,3),("a","b","ab"),([1,2],[3],[1,2,3])],
                            ids=["num","str","lst"])
    def test_s_add(self,x,y,z):
        assert sample_add(x,y) == z
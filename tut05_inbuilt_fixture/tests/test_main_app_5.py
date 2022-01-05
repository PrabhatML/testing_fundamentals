import json
import os
from tut05_inbuilt_fixture.main_app.app import save_dict

# tmpdir create temp directory
# capsys is used to read system output
def test_save_dict(tmpdir,capsys):
    filepath = os.path.join(tmpdir,"test.json")
    _dict = {"a":1,"b":2}
    save_dict(_dict,filepath)
    assert json.load(open(filepath,'r')) == _dict
    assert capsys.readouterr().out == "saved\n"
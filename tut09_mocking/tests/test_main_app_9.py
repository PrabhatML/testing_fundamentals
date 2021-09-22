from tut09_mocking.main_app.sample import guess_number,get_ip
from unittest import mock
import pytest


@pytest.mark.parametrize("_input,expected",[(3,"you won!"),(4,"you lost!")])
@mock.patch('tut09_mocking.main_app.sample.roll_dice')
def test_guess_number(mock_roll_dice,_input,expected):
    mock_roll_dice.return_value = _input
    assert guess_number(3) == expected
    mock_roll_dice.assert_called()


@mock.patch('tut09_mocking.main_app.sample.requests.get')
def test_get_ip(mock_request_get):
    mock_request_get.return_value = mock.Mock(name="mock response",
                                            **{"status_code":200,"json.return_value":{"origin":"0.0.0.0"}})
    assert get_ip() == "0.0.0.0"
    mock_request_get.assert_called_with("https://httpbin.org/ip")


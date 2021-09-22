from unittest import mock
import pytest
from unittest.mock import call
from tut10_adv_mocking.main_app.sample import random_sum,silly


# Use of side effect
@mock.patch('tut10_adv_mocking.main_app.sample.random.randint')
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3,4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1,10),call(1,10)])



@mock.patch('tut10_adv_mocking.main_app.sample.random.randint')
@mock.patch('tut10_adv_mocking.main_app.sample.time.time')
@mock.patch('tut10_adv_mocking.main_app.sample.requests.get')
def test_silly(mock_requests_get,mock_time,mock_randind):
    test_params = {
        "timestamp" : 123,
        "number" : 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randind.return_value = 5
    mock_requests_get.return_value = mock.Mock(**{"status_code":200,
                                "json.return_value":{"args":test_params}})

    assert silly() == test_params

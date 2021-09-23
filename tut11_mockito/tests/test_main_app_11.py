from tut11_mockito.main_app.sample import get_text,Dog

from mockito import when,mock,unstub,verify,kwargs
from mockito.invocation import InvocationError
import os
import pytest
import requests


def test_exists_any():
    with when(os.path).exists(...).thenReturn(True):
        assert os.path.exists("/bar") == True

def test_exists_foo():
    with when(os.path).exists("/foo").thenReturn(True):
        assert os.path.exists("/foo") == True

def test_exists_foo_false():
    with when(os.path).exists("/foo").thenReturn(True) and  pytest.raises(InvocationError):
        assert os.path.exists("/bar") == False


def test_get_text():
    response = mock({
        'status_code':200,
        'text':'Ok'
    },spec=requests.Response)
    with when(requests).get('https://example.com/api').thenReturn(response):
        assert get_text('https://example.com/api') == 'Ok'

def test_dog_bark():
    with when(Dog).bark().thenReturn("Miau!"):
        rex = Dog()
        assert rex.bark() == "Miau!"

        with when(rex).bark().thenReturn("Grrrrr"):
            assert rex.bark() == 'Grrrrr'

        assert Dog().bark() == "Miau!"

def test_dog_action():
    bobby = Dog()
    when(Dog).action("roll",**kwargs).thenReturn("Done")
    assert bobby.action("roll",command="up") == "Done"

    # checking number of times function is being called
    verify(Dog,times=1).action('roll', command='up')
    unstub()
import pytest
from app.extension import some_extension_function


def test_some_extension_function():
    result = some_extension_function('input')
    assert result == 'expected_output'
import pytest
from app import hello_world, broken_function

def test_hello():
    assert hello_world() == "Docker ready"

def test_broken():  # This will fail
    broken_function()

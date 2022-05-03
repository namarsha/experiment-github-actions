from src.cicd import *
import pytest

def test_firsttest():
    assert check_test() == 42

def test_secondtest():
    assert lamas() == 1357
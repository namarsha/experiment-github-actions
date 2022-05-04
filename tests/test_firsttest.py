from src.cicd import *
import pytest

def test_firsttest():
    assert check_test() == 42

def test_secondtest():
    assert lamas() == 1357

def test_thirdtest():
    assert 5 == 5
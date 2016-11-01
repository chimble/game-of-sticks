from sticks import main
from sticks import initial_sticks
from sticks import choose_number
from sticks import current_sticks

def test_main_exists():
    assert main

def test_initial_sticks():
    assert initial_sticks() == 20

def test_choose_number():
    assert 1 <= choose_number() <= 3

def test_current_sticks():
    assert initial_sticks() - choose_number() == 18

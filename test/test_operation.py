from src.math_stuff import add, sub


def test_add():
    assert add(2,3) ==  5
    assert add(-1,0) ==  -1
    assert add(4,-3) ==  1


def test_add():
    assert sub(2,3) ==  -1
    assert sub(-1,0) ==  -1
    assert sub(4,-3) ==  7
    assert sub(4,-10) ==  7





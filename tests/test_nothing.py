import pytest

from maybe import Maybe, Just, Nothing


def test_new_instance():
    x = Maybe(None)
    assert isinstance(x, Maybe)
    assert not isinstance(x, Just)
    assert isinstance(x, Nothing)


def test_attributes():
    x = Maybe(None)
    assert not x
    assert x.is_defined() is False
    assert x.is_empty() is True


def test_iteration():
    x = Maybe(None)
    assert list(iter(x)) == []
    for _ in x:
        assert False


def test_next():
    with pytest.raises(TypeError):
        _ = next(Maybe(None))


def test_contains():
    x = Maybe(None)
    assert 5 not in x
    assert None in x


def test_map():
    assert None in Maybe(None).map(str)


def test_filter():
    x = Maybe(None).filter(lambda v: v == 5)
    assert isinstance(x, Nothing)
    assert None in x


def test_remove():
    x = Maybe(None).remove(4)
    assert isinstance(x, Nothing)
    assert None in x


def test_get():
    with pytest.raises(TypeError):
        _ = Maybe(None).get()


def test_get_or_else():
    assert Maybe(None).get_or_else(6) == 6

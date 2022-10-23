import pytest

from maybe import Maybe, Just, Nothing


def test_new_instance():
    x = Maybe(5)
    assert isinstance(x, Maybe)
    assert isinstance(x, Just)
    assert not isinstance(x, Nothing)


def test_attributes():
    x = Maybe(5)
    assert x
    assert x.is_defined() is True
    assert x.is_empty() is False


def test_iteration():
    x = Maybe(5)
    assert list(iter(x)) == [5]
    for value in x:
        assert value == 5


def test_next():
    assert next(Maybe(5)) == 5


def test_contains():
    x = Maybe(5)
    assert 5 in x
    assert None not in x


def test_map():
    assert Maybe(5).map(str).get() == "5"


def test_filter_keep():
    x = Maybe(5).filter(lambda v: v == 5)
    assert isinstance(x, Just)
    assert 5 in x


def test_filter_lose():
    x = Maybe(5).filter(lambda v: v == 6)
    assert isinstance(x, Nothing)
    assert None in x


def test_remove_keep():
    x = Maybe(5).remove(4)
    assert isinstance(x, Just)
    assert 5 in x


def test_remove_lose():
    x = Maybe(5).remove(5)
    assert isinstance(x, Nothing)
    assert None in x


def test_get():
    assert Maybe(5).get() == 5


def test_get_or_else():
    assert Maybe(5).get_or_else(6) == 5

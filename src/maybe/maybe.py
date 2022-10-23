from typing import Optional, TypeVar, Generic, Iterator, Callable, Union

T = TypeVar("T")
S = TypeVar("S")


class Maybe(Generic[T]):
    def __new__(cls, value: Optional[T] = None) -> "Maybe[T]":
        if value is not None:
            return Just(value)
        else:
            return Nothing()

    def __iter__(self) -> Iterator[T]:
        ...

    def __next__(self) -> T:
        ...

    def __contains__(self, item: T) -> bool:
        ...

    def __eq__(self, other: "Maybe") -> bool:
        ...

    def __bool__(self) -> bool:
        ...

    def is_empty(self) -> bool:
        ...

    def is_defined(self) -> bool:
        ...

    def map(self, fn: Callable[[T], S]) -> "Maybe[S]":
        ...

    def filter(self, fn: Callable[[T], bool]) -> "Maybe[T]":
        ...

    def remove(self, *args: T) -> "Maybe[T]":
        ...

    def get(self) -> T:
        ...

    def get_or_else(self, default: S) -> Union[T, S]:
        ...


class Just(Maybe[T]):
    def __repr__(self):
        return f"Just({self.__value})"

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, value: T):
        self.__value: T = value

    def __iter__(self) -> Iterator[T]:
        return [self.__value].__iter__()

    def __next__(self) -> T:
        return self.__value

    def __contains__(self, item: T) -> bool:
        return item == self.__value

    def __eq__(self, other: "Maybe") -> bool:
        return self.__value in other

    def __bool__(self) -> bool:
        return True

    def is_empty(self) -> bool:
        return False

    def is_defined(self) -> bool:
        return True

    def map(self, fn: Callable[[T], S]) -> Maybe[S]:
        return Maybe(fn(self.__value))

    def filter(self, fn: Callable[[T], bool]) -> Maybe[T]:
        return Maybe(self.__value if fn(self.__value) is True else None)

    def remove(self, *args: T) -> "Maybe[T]":
        for value in args:
            if value in self:
                return Nothing()
        return self

    def get(self) -> T:
        return self.__value

    def get_or_else(self, default: S) -> Union[T, S]:
        return self.__value


class Nothing(Maybe[T]):
    def __repr__(self):
        return "Nothing()"

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, value: None = None):
        self.__value = value

    def __iter__(self) -> Iterator[T]:
        return [].__iter__()

    def __next__(self) -> T:
        raise TypeError("next(Nothing)")

    def __contains__(self, item: T) -> bool:
        return item is None

    def __eq__(self, other: "Maybe") -> bool:
        return isinstance(other, Nothing)

    def __bool__(self) -> bool:
        return False

    def is_empty(self) -> bool:
        return True

    def is_defined(self) -> bool:
        return False

    def map(self, fn: Callable[[T], S]) -> "Nothing":
        return Nothing()

    def filter(self, fn: Callable[[T], bool]) -> Maybe[T]:
        return Nothing()

    def remove(self, *args: T) -> "Maybe[T]":
        return self

    def get(self) -> T:
        raise TypeError("Nothing.get")

    def get_or_else(self, default: S) -> Union[T, S]:
        return default

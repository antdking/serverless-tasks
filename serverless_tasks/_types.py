from typing import TypeVar, Protocol


_F = TypeVar("_F")


class ITask(Protocol[_F]):
    __call__: _F

    def __init__(self, fn: _F):
        ...

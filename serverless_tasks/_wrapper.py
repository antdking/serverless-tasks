from typing import Callable, Optional, Type, TYPE_CHECKING, TypeVar, cast

from ._types import ITask


_F = TypeVar("_F")


def task(**kwargs) -> Callable[[_F], "ITask[_F]"]:
    # We're using ITask to spoof the callable type, so ignore
    # that Task behaves subtly different.
    # PEP612 should solve this for us.
    return Task  # type: ignore


class Task:
    def __init__(self, fn: Callable):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

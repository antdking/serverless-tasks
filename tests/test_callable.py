import pytest
from serverless_tasks import task


# Prove that a task behaves like a normal function when called
# like a normal function


def test_a_task_can_be_called_normally():
    @task()
    def a_function():
        return 42

    assert a_function() == 42


def test_a_task_can_be_called_with_args():
    @task()
    def a_function(x):
        return x

    assert a_function(54) == 54


@pytest.mark.asyncio
async def test_an_async_task_can_be_called_normally():
    @task()
    async def a_function():
        return 42

    assert await a_function() == 42


@pytest.mark.asyncio
async def test_an_async_task_can_be_called_with_args():
    @task()
    async def a_function(x):
        return x

    assert await a_function(54) == 54

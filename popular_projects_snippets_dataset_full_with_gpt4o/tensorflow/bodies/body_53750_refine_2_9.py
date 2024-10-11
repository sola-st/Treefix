from unittest import mock # pragma: no cover
import functools # pragma: no cover
import typing # pragma: no cover

parameterized = type('Mock', (object,), {'named_parameters': mock.Mock()}) # pragma: no cover
f = mock.Mock() # pragma: no cover
context = type('Mock', (object,), {'execution_mode': mock.Mock(), 'ASYNC': 'ASYNC', 'SYNC': 'SYNC'}) # pragma: no cover

from parameterized import parameterized # pragma: no cover
import functools # pragma: no cover

class MockParameterized:# pragma: no cover
    @staticmethod# pragma: no cover
    def named_parameters(params):# pragma: no cover
        def decorator(f):# pragma: no cover
            def wrapper(*args, **kwargs):# pragma: no cover
                for name, value in params:# pragma: no cover
                    f(*args, **{**kwargs, 'async_mode': value})# pragma: no cover
            return wrapper# pragma: no cover
        return decorator# pragma: no cover
parameterized = MockParameterized # pragma: no cover
f = lambda self, *args, **kwargs: print('Function executed with args:', args, 'and kwargs:', kwargs) # pragma: no cover
class MockExecutionMode:# pragma: no cover
    def __init__(self, mode):# pragma: no cover
        self.mode = mode# pragma: no cover
    def __enter__(self):# pragma: no cover
        print('Entering mode:', self.mode)# pragma: no cover
    def __exit__(self, exc_type, exc_val, exc_tb):# pragma: no cover
        print('Exiting mode:', self.mode)# pragma: no cover
context = type('MockContext', (object,), {'execution_mode': MockExecutionMode, 'ASYNC': 'async', 'SYNC': 'sync'}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
from l3.Runtime import _l_
"""Execute the test in async mode and sync mode."""

@parameterized.named_parameters([("Async", True), ("", False)])
@functools.wraps(f)
def decorator(self, async_mode, *args, **kwargs):
    _l_(22440)

    if async_mode:
        _l_(22439)

        with context.execution_mode(context.ASYNC):
            _l_(22436)

            f(self, *args, **kwargs)
            _l_(22435)
    else:
        with context.execution_mode(context.SYNC):
            _l_(22438)

            f(self, *args, **kwargs)
            _l_(22437)
aux = decorator
_l_(22441)
exit(aux)

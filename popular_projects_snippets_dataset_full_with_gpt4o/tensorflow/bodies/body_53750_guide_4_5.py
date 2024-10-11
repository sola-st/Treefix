import functools # pragma: no cover
from parameterized import parameterized # pragma: no cover
import contextlib # pragma: no cover

@contextlib.contextmanager # pragma: no cover
def mock_execution_mode(mode): # pragma: no cover
    print(f'Entering {mode} mode') # pragma: no cover
    yield # pragma: no cover
    print(f'Exiting {mode} mode') # pragma: no cover
 # pragma: no cover
context = type('MockContext', (object,), { # pragma: no cover
    'ASYNC': 'async', # pragma: no cover
    'SYNC': 'sync', # pragma: no cover
    'execution_mode': mock_execution_mode # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs): # pragma: no cover
    print(f'Function executed with args: {args}, kwargs: {kwargs}') # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover

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

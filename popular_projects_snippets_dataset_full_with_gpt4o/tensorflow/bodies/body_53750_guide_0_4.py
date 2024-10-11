import functools # pragma: no cover
from parameterized import parameterized # pragma: no cover

def f(self, *args, **kwargs): pass # pragma: no cover
class MockContext: # pragma: no cover
    class execution_mode: # pragma: no cover
        SYNC = 'sync' # pragma: no cover
        ASYNC = 'async' # pragma: no cover
        def __init__(self, mode): # pragma: no cover
            self.mode = mode # pragma: no cover
context = MockContext() # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover

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

import functools # pragma: no cover
import contextlib as context # pragma: no cover

class MockContext: # pragma: no cover
    ASYNC = 'async' # pragma: no cover
    SYNC = 'sync' # pragma: no cover
 # pragma: no cover
    def execution_mode(self, mode): # pragma: no cover
        yield # pragma: no cover
 # pragma: no cover
context = MockContext() # pragma: no cover
 # pragma: no cover
def f(self, *args, **kwargs): # pragma: no cover
    print('Function executed with async_mode:', kwargs.get('async_mode', False)) # pragma: no cover
 # pragma: no cover
class TestClass: # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
self = TestClass() # pragma: no cover

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

from parameterized import parameterized # pragma: no cover
import functools # pragma: no cover

f = lambda self, *args, **kwargs: None # pragma: no cover
context = type('MockContext', (object,), {'ASYNC': 'async_mode', 'SYNC': 'sync_mode', 'execution_mode': lambda self, mode: self}) # pragma: no cover

from parameterized import parameterized # pragma: no cover
import functools # pragma: no cover

class MockParameterized: # pragma: no cover
    @staticmethod # pragma: no cover
    def named_parameters(params): # pragma: no cover
        def decorator(f): # pragma: no cover
            def wrapper(*args, **kwargs): # pragma: no cover
                for name, async_mode in params: # pragma: no cover
                    f(*args, async_mode=async_mode, **kwargs) # pragma: no cover
            return wrapper # pragma: no cover
        return decorator # pragma: no cover
 # pragma: no cover
parameterized = MockParameterized() # pragma: no cover
f = lambda self, *args, **kwargs: None # pragma: no cover
class MockContext: # pragma: no cover
    ASYNC = 'async_mode' # pragma: no cover
    SYNC = 'sync_mode' # pragma: no cover
    class execution_mode: # pragma: no cover
        def __init__(self, mode): # pragma: no cover
            self.mode = mode # pragma: no cover
        def __enter__(self): # pragma: no cover
            pass # pragma: no cover
        def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
            pass # pragma: no cover
 # pragma: no cover
context = MockContext() # pragma: no cover

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

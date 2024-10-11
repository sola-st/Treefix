from parameterized import parameterized # pragma: no cover
import functools # pragma: no cover
def f(self, *args, **kwargs): pass # pragma: no cover
class Context: pass # pragma: no cover
context = Context() # pragma: no cover

context.execution_mode = type('Mock', (object,), {'__enter__': lambda self: None, '__exit__': lambda self, exc_type, exc_value, traceback: None}) # pragma: no cover
context.ASYNC = 'async' # pragma: no cover
context.SYNC = 'sync' # pragma: no cover

import functools # pragma: no cover
from parameterized import parameterized # pragma: no cover
def f(self, *args, **kwargs): return f'Function executed with: {args} {kwargs}' # pragma: no cover

def named_parameters(param_list): # pragma: no cover
    def decorator(func): return func # pragma: no cover
    return decorator(param_list) # pragma: no cover
parameterized.named_parameters = named_parameters # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
from l3.Runtime import _l_
"""Execute the test in async mode and sync mode."""

@parameterized.named_parameters([("Async", True), ("", False)])
@functools.wraps(f)
def decorator(self, async_mode, *args, **kwargs):
    _l_(10171)

    if async_mode:
        _l_(10170)

        with context.execution_mode(context.ASYNC):
            _l_(10167)

            f(self, *args, **kwargs)
            _l_(10166)
    else:
        with context.execution_mode(context.SYNC):
            _l_(10169)

            f(self, *args, **kwargs)
            _l_(10168)
aux = decorator
_l_(10172)
exit(aux)

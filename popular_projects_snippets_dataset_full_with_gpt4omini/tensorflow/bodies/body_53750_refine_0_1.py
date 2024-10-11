f = lambda self, *args, **kwargs: None # pragma: no cover
context = type('Mock', (), {'execution_mode': lambda mode: None, 'ASYNC': 'async', 'SYNC': 'sync'}) # pragma: no cover

def mock_execution_mode(mode): pass # pragma: no cover
parameterized = type('Mock', (), {'named_parameters': lambda params: lambda f: f})() # pragma: no cover
f = lambda self, *args, **kwargs: None # pragma: no cover
context = type('Mock', (), {'execution_mode': mock_execution_mode, 'ASYNC': 'async', 'SYNC': 'sync'}) # pragma: no cover

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

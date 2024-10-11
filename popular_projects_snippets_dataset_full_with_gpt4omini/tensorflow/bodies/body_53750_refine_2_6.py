def f(self, *args, **kwargs): return 'Function executed' # pragma: no cover

def f(self, *args, **kwargs): return 'Function executed' # pragma: no cover

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

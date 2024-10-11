from functools import wraps # pragma: no cover
from unittest import mock # pragma: no cover

parameterized = type('Mock', (object,), {'named_parameters': mock.Mock()}) # pragma: no cover
f = mock.Mock() # pragma: no cover
context = type('Mock', (object,), {'execution_mode': mock.Mock(), 'ASYNC': 'async', 'SYNC': 'sync'}) # pragma: no cover

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

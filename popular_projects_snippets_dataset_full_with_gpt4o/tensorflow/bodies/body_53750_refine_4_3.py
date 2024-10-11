from unittest.mock import Mock # pragma: no cover
import functools # pragma: no cover

f = Mock() # pragma: no cover
context = type('Context', (object,), {'execution_mode': Mock(return_value=Mock(__enter__=lambda s: None, __exit__=lambda s, exc_type, exc_val, exc_tb: None)), 'ASYNC': 'ASYNC', 'SYNC': 'SYNC'})() # pragma: no cover

import functools # pragma: no cover
import contextlib # pragma: no cover

parameterized = type('MockParameterized', (object,), {'named_parameters': lambda params: (lambda f: f)})() # pragma: no cover
f = lambda self, *args, **kwargs: None # pragma: no cover
context = type('MockContext', (object,), {'ASYNC': 'async', 'SYNC': 'sync', 'execution_mode': lambda self, mode: contextlib.nullcontext()})() # pragma: no cover

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

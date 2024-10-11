from unittest import mock # pragma: no cover
from unittest.mock import Mock # pragma: no cover

parameterized = Mock() # pragma: no cover
parameterized.named_parameters = mock.MagicMock() # pragma: no cover
functools = Mock() # pragma: no cover
functools.wraps = mock.MagicMock() # pragma: no cover
f = Mock() # pragma: no cover
context = Mock() # pragma: no cover
context.execution_mode = mock.MagicMock() # pragma: no cover
context.ASYNC = 'ASYNC' # pragma: no cover
context.SYNC = 'SYNC' # pragma: no cover

import functools # pragma: no cover

parameterized = type('MockParameterized', (object,), {'named_parameters': lambda params: lambda f: f})() # pragma: no cover
f = lambda self, *args, **kwargs: None # pragma: no cover
context = type('MockContext', (object,), {'execution_mode': lambda mode: contextlib.nullcontext(), 'ASYNC': 'ASYNC', 'SYNC': 'SYNC'})() # pragma: no cover

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

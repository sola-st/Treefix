import sys # pragma: no cover
import types # pragma: no cover

sys.exc_info = lambda: (None, None, types.TracebackType(tb_frame=types.FrameType(f_code=None, f_globals={}, f_locals={}, f_lineno=0, f_lasti=0, f_back=None), tb_lineno=0, tb_next=None)) # pragma: no cover
f = type('Mock', (object,), {'__code__': None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Check whether calling a function raised a ``TypeError`` because
    the call failed or because something in the factory raised the
    error.

    :param f: The function that was called.
    :return: ``True`` if the call failed.
    """
tb = sys.exc_info()[2]
_l_(20706)

try:
    _l_(20714)

    while tb is not None:
        _l_(20710)

        if tb.tb_frame.f_code is f.__code__:
            _l_(20708)

            aux = False
            _l_(20707)
            # In the function, it was called successfully.
            exit(aux)

        tb = tb.tb_next
        _l_(20709)
    aux = True
    _l_(20711)

    # Didn't reach the function.
    exit(aux)
finally:
    _l_(20713)

    # Delete tb to break a circular reference.
    # https://docs.python.org/2/library/sys.html#sys.exc_info
    del tb
    _l_(20712)

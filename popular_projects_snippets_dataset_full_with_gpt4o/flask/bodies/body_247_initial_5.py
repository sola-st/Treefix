import sys # pragma: no cover
import types # pragma: no cover

sys = type('MockSys', (object,), {'exc_info': lambda: (None, None, type('MockTb', (object,), {'tb_frame': None, 'tb_next': None})())})() # pragma: no cover
f = type('MockFunction', (object,), {'__code__': type('MockCode', (object,), {})()}) # pragma: no cover

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
_l_(20754)

try:
    _l_(20762)

    while tb is not None:
        _l_(20758)

        if tb.tb_frame.f_code is f.__code__:
            _l_(20756)

            aux = False
            _l_(20755)
            # In the function, it was called successfully.
            exit(aux)

        tb = tb.tb_next
        _l_(20757)
    aux = True
    _l_(20759)

    # Didn't reach the function.
    exit(aux)
finally:
    _l_(20761)

    # Delete tb to break a circular reference.
    # https://docs.python.org/2/library/sys.html#sys.exc_info
    del tb
    _l_(20760)

import sys # pragma: no cover

def mock_function(): pass # pragma: no cover
class MockCode: pass # pragma: no cover
class MockFrame: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.f_code = MockCode() # pragma: no cover
class MockTraceback: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.tb_frame = MockFrame() # pragma: no cover
        self.tb_next = None # pragma: no cover
sys.exc_info = lambda: (None, None, MockTraceback()) # pragma: no cover
f = mock_function # pragma: no cover

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
_l_(9541)

try:
    _l_(9549)

    while tb is not None:
        _l_(9545)

        if tb.tb_frame.f_code is f.__code__:
            _l_(9543)

            aux = False
            _l_(9542)
            # In the function, it was called successfully.
            exit(aux)

        tb = tb.tb_next
        _l_(9544)
    aux = True
    _l_(9546)

    # Didn't reach the function.
    exit(aux)
finally:
    _l_(9548)

    # Delete tb to break a circular reference.
    # https://docs.python.org/2/library/sys.html#sys.exc_info
    del tb
    _l_(9547)

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
from l3.Runtime import _l_
try:
    _l_(12808)

    do_something()
    _l_(12805)
except Exception:
    _l_(12807)

    pass
    _l_(12806)

try:
    _l_(12812)

    do_something()
    _l_(12809)
except Exception:
    _l_(12811)

    sys.exc_clear()
    _l_(12810)


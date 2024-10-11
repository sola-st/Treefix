import sys # pragma: no cover
import random # pragma: no cover

def do_something(): # pragma: no cover
    if random.choice([True, False]): # pragma: no cover
        raise Exception('An error occurred') # pragma: no cover
    return 'Success' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
from l3.Runtime import _l_
try:
    _l_(682)

    do_something()
    _l_(679)
except Exception:
    _l_(681)

    pass
    _l_(680)

try:
    _l_(686)

    do_something()
    _l_(683)
except Exception:
    _l_(685)

    sys.exc_clear()
    _l_(684)


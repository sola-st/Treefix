class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self._got_first_request = False # pragma: no cover

self = Mock() # pragma: no cover
f_name = 'setup' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
if self._got_first_request:
    _l_(4584)

    raise AssertionError(
        f"The setup method '{f_name}' can no longer be called"
        " on the application. It has already handled its first"
        " request, any changes will not be applied"
        " consistently.\n"
        "Make sure all imports, decorators, functions, etc."
        " needed to set up the application are done before"
        " running it."
    )
    _l_(4583)

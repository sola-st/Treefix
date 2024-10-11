view_func = type('MockViewFunc', (object,), {'__name__': 'example_function_name'})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Internal helper that returns the default endpoint for a given
    function.  This always is the function name.
    """
assert view_func is not None, "expected view func if endpoint is not provided."
_l_(22502)
aux = view_func.__name__
_l_(22503)
exit(aux)

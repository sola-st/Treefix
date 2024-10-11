self = type('Mock', (object,), {'url_default_functions': {None: []}})() # pragma: no cover
f = lambda x: x # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Callback function for URL defaults for all view functions of the
        application.  It's called with the endpoint and values and should
        update the values passed in place.
        """
self.url_default_functions[None].append(f)
_l_(17704)
aux = f
_l_(17705)
exit(aux)

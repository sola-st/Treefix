from collections import defaultdict # pragma: no cover
from flask import g # pragma: no cover

self = type('Mock', (object,), {'url_value_preprocessors': defaultdict(list)})() # pragma: no cover
f = lambda endpoint, values: None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Register a URL value preprocessor function for all view
        functions in the application. These functions will be called before the
        :meth:`before_request` functions.

        The function can modify the values captured from the matched url before
        they are passed to the view. For example, this can be used to pop a
        common language code value and place it in ``g`` rather than pass it to
        every view.

        The function is passed the endpoint name and values dict. The return
        value is ignored.
        """
self.url_value_preprocessors[None].append(f)
_l_(4576)
aux = f
_l_(4577)
exit(aux)

f = lambda: print('Function f executed') # pragma: no cover
self = type('Mock', (object,), {'record_once': lambda self, func: func(self)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Like :meth:`Flask.before_first_request`.  Such a function is
        executed before the first request to the application.

        .. deprecated:: 2.2
            Will be removed in Flask 2.3. Run setup code when creating
            the application instead.
        """
try:
    import warnings
    _l_(20065)

except ImportError:
    pass

warnings.warn(
    "'before_app_first_request' is deprecated and will be"
    " removed in Flask 2.3. Use 'record_once' instead to run"
    " setup code when registering the blueprint.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(20066)
self.record_once(lambda s: s.app.before_first_request_funcs.append(f))
_l_(20067)
aux = f
_l_(20068)
exit(aux)

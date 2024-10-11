import json # pragma: no cover
import warnings # pragma: no cover

class MockApp:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._json_decoder = None# pragma: no cover
        self.blueprints = {} # pragma: no cover
class MockBlueprint:# pragma: no cover
    def __init__(self):# pragma: no cover
        self._json_decoder = None # pragma: no cover
class MockRequest:# pragma: no cover
    def __init__(self, blueprint):# pragma: no cover
        self.blueprint = blueprint # pragma: no cover
self = type('Mock', (), {'_app': MockApp()})() # pragma: no cover
bp = MockBlueprint() # pragma: no cover
self._app.blueprints['test_blueprint'] = bp # pragma: no cover
request = MockRequest('test_blueprint') # pragma: no cover
kwargs = {} # pragma: no cover
s = '{"key": "value"}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON from a string or bytes.

        :param s: Text or UTF-8 bytes.
        :param kwargs: Passed to :func:`json.loads`.
        """
cls = self._app._json_decoder
_l_(5596)
bp = self._app.blueprints.get(request.blueprint) if request else None
_l_(5597)

if bp is not None and bp._json_decoder is not None:
    _l_(5599)

    cls = bp._json_decoder
    _l_(5598)

if cls is not None:
    _l_(5604)

    try:
        import warnings
        _l_(5601)

    except ImportError:
        pass

    warnings.warn(
        "Setting 'json_decoder' on the app or a blueprint is"
        " deprecated and will be removed in Flask 2.3."
        " Customize 'app.json' instead.",
        DeprecationWarning,
    )
    _l_(5602)
    kwargs.setdefault("cls", cls)
    _l_(5603)
aux = json.loads(s, **kwargs)
_l_(5605)

exit(aux)

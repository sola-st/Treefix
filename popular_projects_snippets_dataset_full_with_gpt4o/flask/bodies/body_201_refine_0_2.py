import json # pragma: no cover
import warnings # pragma: no cover

self = type('MockApp', (object,), {'_app': type('MockAppInner', (object,), {'_json_decoder': None, 'blueprints': {'demo_blueprint': type('MockBlueprint', (object,), {'_json_decoder': None})()}})()})() # pragma: no cover
request = type('MockRequest', (object,), {'blueprint': 'demo_blueprint'})() # pragma: no cover
kwargs = {} # pragma: no cover
s = '{"key": "value"}' # pragma: no cover

import json # pragma: no cover

self = type('MockApp', (object,), {'_app': type('MockAppInner', (object,), {'_json_decoder': json.JSONDecoder, 'blueprints': {'demo_blueprint': type('MockBlueprint', (object,), {'_json_decoder': None})()}})()})() # pragma: no cover
request = type('MockRequest', (object,), {'blueprint': 'demo_blueprint'})() # pragma: no cover
kwargs = dict() # pragma: no cover
s = '{"key": "value"}' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON from a string or bytes.

        :param s: Text or UTF-8 bytes.
        :param kwargs: Passed to :func:`json.loads`.
        """
cls = self._app._json_decoder
_l_(17300)
bp = self._app.blueprints.get(request.blueprint) if request else None
_l_(17301)

if bp is not None and bp._json_decoder is not None:
    _l_(17303)

    cls = bp._json_decoder
    _l_(17302)

if cls is not None:
    _l_(17308)

    try:
        import warnings
        _l_(17305)

    except ImportError:
        pass

    warnings.warn(
        "Setting 'json_decoder' on the app or a blueprint is"
        " deprecated and will be removed in Flask 2.3."
        " Customize 'app.json' instead.",
        DeprecationWarning,
    )
    _l_(17306)
    kwargs.setdefault("cls", cls)
    _l_(17307)
aux = json.loads(s, **kwargs)
_l_(17309)

exit(aux)

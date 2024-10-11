# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/json/provider.py
from l3.Runtime import _l_
"""Deserialize data as JSON from a string or bytes.

        :param s: Text or UTF-8 bytes.
        :param kwargs: Passed to :func:`json.loads`.
        """
cls = self._app._json_decoder
_l_(17361)
bp = self._app.blueprints.get(request.blueprint) if request else None
_l_(17362)

if bp is not None and bp._json_decoder is not None:
    _l_(17364)

    cls = bp._json_decoder
    _l_(17363)

if cls is not None:
    _l_(17369)

    try:
        import warnings
        _l_(17366)

    except ImportError:
        pass

    warnings.warn(
        "Setting 'json_decoder' on the app or a blueprint is"
        " deprecated and will be removed in Flask 2.3."
        " Customize 'app.json' instead.",
        DeprecationWarning,
    )
    _l_(17367)
    kwargs.setdefault("cls", cls)
    _l_(17368)
aux = json.loads(s, **kwargs)
_l_(17370)

exit(aux)

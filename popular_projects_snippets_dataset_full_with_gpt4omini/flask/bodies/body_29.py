# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Blueprint-local JSON encoder class to use. Set to ``None`` to use the app's.

        .. deprecated:: 2.2
             Will be removed in Flask 2.3. Customize
             :attr:`json_provider_class` instead.

        .. versionadded:: 0.10
        """
try:
    import warnings
    _l_(5593)

except ImportError:
    pass

warnings.warn(
    "'bp.json_encoder' is deprecated and will be removed in Flask 2.3."
    " Customize 'app.json_provider_class' or 'app.json' instead.",
    DeprecationWarning,
    stacklevel=2,
)
_l_(5594)
aux = self._json_encoder
_l_(5595)
exit(aux)

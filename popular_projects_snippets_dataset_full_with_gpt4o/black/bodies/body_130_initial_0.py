import warnings # pragma: no cover

self = type('MockSelf', (object,), {'experimental_string_processing': True})() # pragma: no cover
warn = warnings.warn # pragma: no cover
Deprecated = type('Deprecated', (Warning,), {}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
if self.experimental_string_processing:
    _l_(18893)

    warn(
        (
            "`experimental string processing` has been included in `preview`"
            " and deprecated. Use `preview` instead."
        ),
        Deprecated,
    )
    _l_(18892)

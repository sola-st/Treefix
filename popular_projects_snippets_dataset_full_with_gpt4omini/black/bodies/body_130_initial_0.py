class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.experimental_string_processing = True # pragma: no cover
def warn(message, category): print(f'Warning: {message}, Category: {category}') # pragma: no cover
warn = warn # pragma: no cover
class Deprecated: pass # pragma: no cover
Deprecated = Deprecated # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/mode.py
from l3.Runtime import _l_
if self.experimental_string_processing:
    _l_(7319)

    warn(
        (
            "`experimental string processing` has been included in `preview`"
            " and deprecated. Use `preview` instead."
        ),
        Deprecated,
    )
    _l_(7318)

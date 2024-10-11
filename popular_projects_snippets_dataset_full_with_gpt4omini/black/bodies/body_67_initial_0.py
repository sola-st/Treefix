from typing import Dict, List # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._CUSTOM_SPLIT_MAP: Dict[str, List[str]] = {'example_key': ['split1', 'split2']} # pragma: no cover
self._get_key = lambda s: 'example_key' if s == 'example_string' else None # pragma: no cover
string = 'example_string' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""Custom Split Map Getter Method

        Returns:
            * A list of the custom splits that are mapped to @string, if any
            exist.
                OR
            * [], otherwise.

        Side Effects:
            Deletes the mapping between @string and its associated custom
            splits (which are returned to the caller).
        """
key = self._get_key(string)
_l_(5702)

custom_splits = self._CUSTOM_SPLIT_MAP[key]
_l_(5703)
del self._CUSTOM_SPLIT_MAP[key]
_l_(5704)
aux = list(custom_splits)
_l_(5705)

exit(aux)

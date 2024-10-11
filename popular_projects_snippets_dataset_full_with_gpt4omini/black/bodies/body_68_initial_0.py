from typing import Dict # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self._CUSTOM_SPLIT_MAP = {"example_key": "example_value"} # pragma: no cover
def mock_get_key(string): return string[::-1] # pragma: no cover
self._get_key = mock_get_key # pragma: no cover
string = "test" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Returns:
            True iff @string is associated with a set of custom splits.
        """
key = self._get_key(string)
_l_(4158)
aux = key in self._CUSTOM_SPLIT_MAP
_l_(4159)
exit(aux)

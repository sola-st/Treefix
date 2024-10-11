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

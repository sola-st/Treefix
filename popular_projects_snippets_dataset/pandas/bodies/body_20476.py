# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
from l3.Runtime import _l_
"""
        If key is NA value, location of index unify as -1.

        Parameters
        ----------
        level_index: Index
        key : label

        Returns
        -------
        loc : int
            If key is NA value, loc is -1
            Else, location of key in index.

        See Also
        --------
        Index.get_loc : The get_loc method for (single-level) index.
        """
if is_scalar(key) and isna(key):
    _l_(21919)

    aux = -1
    _l_(21917)
    exit(aux)
else:
    aux = level_index.get_loc(key)
    _l_(21918)
    exit(aux)

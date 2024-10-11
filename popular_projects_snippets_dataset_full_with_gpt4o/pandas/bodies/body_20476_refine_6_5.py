import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

is_scalar = np.isscalar # pragma: no cover
key = np.nan  # Example key that is an NA value # pragma: no cover
isna = pd.isna # pragma: no cover
level_index = type('Mock', (object,), {'get_loc': lambda self, k: 0})()  # Mock with get_loc method returning 0 for any key # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

is_scalar = np.isscalar # pragma: no cover
key = np.nan # pragma: no cover
isna = pd.isna # pragma: no cover
level_index = type('Mock', (object,), {'get_loc': lambda self, k: 0 if not pd.isna(k) else -1})() # pragma: no cover

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

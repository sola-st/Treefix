import pandas as pd # pragma: no cover

self = type('Mock', (object,), {'_reset_group_selection': lambda self: None, '_make_mask_from_positional_indexer': lambda self, x: [True, True], '_mask_selected_obj': lambda self, mask: pd.DataFrame([['a', 2], ['b', 2]], columns=['A', 'B'])})() # pragma: no cover
n = 1 # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockDataFrame:# pragma: no cover
    def __init__(self, data):# pragma: no cover
        self.data = data# pragma: no cover
        self.df = pd.DataFrame(data, columns=['A', 'B'])# pragma: no cover
    def _reset_group_selection(self):# pragma: no cover
        pass# pragma: no cover
    def _make_mask_from_positional_indexer(self, idx):# pragma: no cover
        if isinstance(idx, slice):# pragma: no cover
            return np.zeros(len(self.data), dtype=bool)[idx]# pragma: no cover
        elif isinstance(idx, list):# pragma: no cover
            return np.array(idx, dtype=bool)# pragma: no cover
        else:# pragma: no cover
            raise ValueError('Unsupported indexer')# pragma: no cover
    def _mask_selected_obj(self, mask):# pragma: no cover
        return self.df[mask]# pragma: no cover
# pragma: no cover
self = MockDataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]]) # pragma: no cover
n = 1 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
from l3.Runtime import _l_
"""
        Return last n rows of each group.

        Similar to ``.apply(lambda x: x.tail(n))``, but it returns a subset of rows
        from the original DataFrame with original index and order preserved
        (``as_index`` flag is ignored).

        Parameters
        ----------
        n : int
            If positive: number of entries to include from end of each group.
            If negative: number of entries to exclude from start of each group.

        Returns
        -------
        Series or DataFrame
            Subset of original Series or DataFrame as determined by n.
        %(see_also)s
        Examples
        --------

        >>> df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]],
        ...                   columns=['A', 'B'])
        >>> df.groupby('A').tail(1)
           A  B
        1  a  2
        3  b  2
        >>> df.groupby('A').tail(-1)
           A  B
        1  a  2
        3  b  2
        """
self._reset_group_selection()
_l_(22423)
if n:
    _l_(22426)

    mask = self._make_mask_from_positional_indexer(slice(-n, None))
    _l_(22424)
else:
    mask = self._make_mask_from_positional_indexer([])
    _l_(22425)
aux = self._mask_selected_obj(mask)
_l_(22427)

exit(aux)

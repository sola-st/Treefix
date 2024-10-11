import pandas as pd # pragma: no cover

self = type('MockSelf', (object,), {})() # pragma: no cover
n = 1 # pragma: no cover
self._reset_group_selection = lambda: None # pragma: no cover
self._make_mask_from_positional_indexer = lambda indexer: [True, False, False, True] # pragma: no cover
self._mask_selected_obj = lambda mask: pd.DataFrame({'A': ['a', 'b'], 'B': [2, 2]}) # pragma: no cover

import pandas as pd # pragma: no cover

df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=['A', 'B']) # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
n = 1 # pragma: no cover
self._reset_group_selection = lambda: None # pragma: no cover
self._make_mask_from_positional_indexer = lambda indexer: slice(-n, None) if n > 0 else slice(None, None) # pragma: no cover
self._mask_selected_obj = lambda mask: df[mask] if isinstance(mask, slice) else df.iloc[mask] # pragma: no cover

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

import pandas as pd # pragma: no cover

class MockGroupHandler: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=['A', 'B']) # pragma: no cover
        self.grouped = self.data.groupby('A') # pragma: no cover
        self.selected_obj = self.data # pragma: no cover
    def _reset_group_selection(self): # pragma: no cover
        pass # pragma: no cover
    def _make_mask_from_positional_indexer(self, indexer): # pragma: no cover
        if isinstance(indexer, slice): # pragma: no cover
            return self.selected_obj.iloc[indexer] # pragma: no cover
        return None # pragma: no cover
    def _mask_selected_obj(self, mask): # pragma: no cover
        return mask # pragma: no cover
self = MockGroupHandler() # pragma: no cover
n = 1 # pragma: no cover

import pandas as pd # pragma: no cover

class MockGroupSelector: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.data = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=['A', 'B']) # pragma: no cover
        self.grouped_data = self.data.groupby('A') # pragma: no cover
    def _reset_group_selection(self): # pragma: no cover
        pass # pragma: no cover
    def _make_mask_from_positional_indexer(self, indexer): # pragma: no cover
        return self.data.index[indexer] if isinstance(indexer, slice) else [] # pragma: no cover
    def _mask_selected_obj(self, mask): # pragma: no cover
        return self.data.loc[mask] # pragma: no cover
self = MockGroupSelector() # pragma: no cover
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
_l_(10832)
if n:
    _l_(10835)

    mask = self._make_mask_from_positional_indexer(slice(-n, None))
    _l_(10833)
else:
    mask = self._make_mask_from_positional_indexer([])
    _l_(10834)
aux = self._mask_selected_obj(mask)
_l_(10836)

exit(aux)

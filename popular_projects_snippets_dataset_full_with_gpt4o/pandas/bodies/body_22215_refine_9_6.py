import pandas as pd # pragma: no cover

self = type('Mock', (object,), {'_reset_group_selection': lambda self: None, '_make_mask_from_positional_indexer': lambda self, indexer: [True, False, True, False], '_mask_selected_obj': lambda self, mask: pd.DataFrame([['a', 2], ['b', 2]], columns=['A', 'B'])})() # pragma: no cover
n = 1 # pragma: no cover

import pandas as pd # pragma: no cover

n = 1 # pragma: no cover
class Mock:# pragma: no cover
    def __init__(self, df):# pragma: no cover
        self.df = df# pragma: no cover
    def _reset_group_selection(self):# pragma: no cover
        pass# pragma: no cover
    def _make_mask_from_positional_indexer(self, idx):# pragma: no cover
        if isinstance(idx, slice):# pragma: no cover
            return self.df.index[idx].tolist()# pragma: no cover
        return idx# pragma: no cover
    def _mask_selected_obj(self, mask):# pragma: no cover
        return self.df.loc[mask]# pragma: no cover
# pragma: no cover
# Example DataFrame from the docstring# pragma: no cover
example_df = pd.DataFrame([['a', 1], ['a', 2], ['b', 1], ['b', 2]], columns=['A', 'B'])# pragma: no cover
example_df = example_df.set_index(pd.Index([0, 1, 2, 3]))# pragma: no cover
self = Mock(example_df) # pragma: no cover

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

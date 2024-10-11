import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.categories = pd.Categorical(['a', 'b', 'c']) # pragma: no cover
        self._codes = np.array([0, 1, 2, -1]) # pragma: no cover
        self.ordered = True # pragma: no cover
    def from_codes(self, codes, categories, ordered): # pragma: no cover
        return pd.Categorical.from_codes(codes, categories, ordered=ordered) # pragma: no cover
self = MockSelf() # pragma: no cover
mapper = lambda x: x.upper() # pragma: no cover

import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.categories = pd.Categorical(['a', 'b', 'c']) # pragma: no cover
        self._codes = np.array([0, 1, 2, -1]) # pragma: no cover
        self.ordered = True # pragma: no cover
    def from_codes(self, codes, categories, ordered): # pragma: no cover
        return pd.Categorical.from_codes(codes, categories, ordered=ordered) # pragma: no cover
self = MockSelf() # pragma: no cover
mapper = {'a': 'A', 'b': 'B', 'c': 'C'} # pragma: no cover
np = type('MockNP', (object,), { # pragma: no cover
    'any': staticmethod(lambda x: any(x)), # pragma: no cover
    'nan': float('nan'), # pragma: no cover
    'take': staticmethod(lambda a, indices: [a[i] if i != -1 else float('nan') for i in indices]) # pragma: no cover
}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
from l3.Runtime import _l_
"""
        Map categories using an input mapping or function.

        Maps the categories to new categories. If the mapping correspondence is
        one-to-one the result is a :class:`~pandas.Categorical` which has the
        same order property as the original, otherwise a :class:`~pandas.Index`
        is returned. NaN values are unaffected.

        If a `dict` or :class:`~pandas.Series` is used any unmapped category is
        mapped to `NaN`. Note that if this happens an :class:`~pandas.Index`
        will be returned.

        Parameters
        ----------
        mapper : function, dict, or Series
            Mapping correspondence.

        Returns
        -------
        pandas.Categorical or pandas.Index
            Mapped categorical.

        See Also
        --------
        CategoricalIndex.map : Apply a mapping correspondence on a
            :class:`~pandas.CategoricalIndex`.
        Index.map : Apply a mapping correspondence on an
            :class:`~pandas.Index`.
        Series.map : Apply a mapping correspondence on a
            :class:`~pandas.Series`.
        Series.apply : Apply more complex functions on a
            :class:`~pandas.Series`.

        Examples
        --------
        >>> cat = pd.Categorical(['a', 'b', 'c'])
        >>> cat
        ['a', 'b', 'c']
        Categories (3, object): ['a', 'b', 'c']
        >>> cat.map(lambda x: x.upper())
        ['A', 'B', 'C']
        Categories (3, object): ['A', 'B', 'C']
        >>> cat.map({'a': 'first', 'b': 'second', 'c': 'third'})
        ['first', 'second', 'third']
        Categories (3, object): ['first', 'second', 'third']

        If the mapping is one-to-one the ordering of the categories is
        preserved:

        >>> cat = pd.Categorical(['a', 'b', 'c'], ordered=True)
        >>> cat
        ['a', 'b', 'c']
        Categories (3, object): ['a' < 'b' < 'c']
        >>> cat.map({'a': 3, 'b': 2, 'c': 1})
        [3, 2, 1]
        Categories (3, int64): [3 < 2 < 1]

        If the mapping is not one-to-one an :class:`~pandas.Index` is returned:

        >>> cat.map({'a': 'first', 'b': 'second', 'c': 'first'})
        Index(['first', 'second', 'first'], dtype='object')

        If a `dict` is used, all unmapped categories are mapped to `NaN` and
        the result is an :class:`~pandas.Index`:

        >>> cat.map({'a': 'first', 'b': 'second'})
        Index(['first', 'second', nan], dtype='object')
        """
new_categories = self.categories.map(mapper)
_l_(20368)
try:
    _l_(20374)

    aux = self.from_codes(
        self._codes.copy(), categories=new_categories, ordered=self.ordered
    )
    _l_(20369)
    exit(aux)
except ValueError:
    _l_(20373)

    # NA values are represented in self._codes with -1
    # np.take causes NA values to take final element in new_categories
    if np.any(self._codes == -1):
        _l_(20371)

        new_categories = new_categories.insert(len(new_categories), np.nan)
        _l_(20370)
    aux = np.take(new_categories, self._codes)
    _l_(20372)
    exit(aux)

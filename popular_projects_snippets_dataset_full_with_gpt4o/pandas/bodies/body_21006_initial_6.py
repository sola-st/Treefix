import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

self = type('Mock', (object,), {'categories': pd.Categorical(['a', 'b', 'c']), 'from_codes': lambda codes, categories, ordered: pd.Categorical.from_codes(codes, categories, ordered), '_codes': np.array([0, 1, 2]), 'ordered': True}) # pragma: no cover
mapper = {'a': 'first', 'b': 'second', 'c': 'third'} # pragma: no cover
np = type('Mock', (object,), {'any': lambda x: np.any(x), 'nan': np.nan, 'take': lambda a, indices: np.take(a, indices)}) # pragma: no cover

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

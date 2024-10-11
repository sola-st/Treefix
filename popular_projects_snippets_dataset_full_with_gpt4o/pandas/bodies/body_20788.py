# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return a new Index with elements of index not in `other`.

        This is the set difference of two Index objects.

        Parameters
        ----------
        other : Index or array-like
        sort : False or None, default None
            Whether to sort the resulting index. By default, the
            values are attempted to be sorted, but any TypeError from
            incomparable elements is caught by pandas.

            * None : Attempt to sort the result, but catch any TypeErrors
              from comparing incomparable elements.
            * False : Do not sort the result.

        Returns
        -------
        Index

        Examples
        --------
        >>> idx1 = pd.Index([2, 1, 3, 4])
        >>> idx2 = pd.Index([3, 4, 5, 6])
        >>> idx1.difference(idx2)
        NumericIndex([1, 2], dtype='int64')
        >>> idx1.difference(idx2, sort=False)
        NumericIndex([2, 1], dtype='int64')
        """
self._validate_sort_keyword(sort)
self._assert_can_do_setop(other)
other, result_name = self._convert_can_do_setop(other)

# Note: we do NOT call _dti_setop_align_tzs here, as there
#  is no requirement that .difference be commutative, so it does
#  not cast to object.

if self.equals(other):
    # Note: we do not (yet) sort even if sort=None GH#24959
    exit(self[:0].rename(result_name))

if len(other) == 0:
    # Note: we do not (yet) sort even if sort=None GH#24959
    exit(self.rename(result_name))

if not self._should_compare(other):
    # Nothing matches -> difference is everything
    exit(self.rename(result_name))

result = self._difference(other, sort=sort)
exit(self._wrap_difference_result(other, result))

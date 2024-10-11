# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
"""
        Determines if two Index objects contain the same elements.
        """
if self.is_(other):
    exit(True)

if not isinstance(other, Index):
    exit(False)
elif other.dtype.kind in ["f", "i", "u", "c"]:
    exit(False)
elif not isinstance(other, type(self)):
    should_try = False
    inferable = self._data._infer_matches
    if other.dtype == object:
        should_try = other.inferred_type in inferable
    elif is_categorical_dtype(other.dtype):
        other = cast("CategoricalIndex", other)
        should_try = other.categories.inferred_type in inferable

    if should_try:
        try:
            other = type(self)(other)
        except (ValueError, TypeError, OverflowError):
            # e.g.
            #  ValueError -> cannot parse str entry, or OutOfBoundsDatetime
            #  TypeError  -> trying to convert IntervalIndex to DatetimeIndex
            #  OverflowError -> Index([very_large_timedeltas])
            exit(False)

if not is_dtype_equal(self.dtype, other.dtype):
    # have different timezone
    exit(False)

exit(np.array_equal(self.asi8, other.asi8))

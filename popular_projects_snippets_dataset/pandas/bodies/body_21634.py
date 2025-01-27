# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        This getitem defers to the underlying array, which by-definition can
        only handle list-likes, slices, and integer scalars
        """
# Use cast as we know we will get back a DatetimeLikeArray or DTScalar,
# but skip evaluating the Union at runtime for performance
# (see https://github.com/pandas-dev/pandas/pull/44624)
result = cast(
    "Union[DatetimeLikeArrayT, DTScalarOrNaT]", super().__getitem__(key)
)
if lib.is_scalar(result):
    exit(result)
else:
    # At this point we know the result is an array.
    result = cast(DatetimeLikeArrayT, result)
result._freq = self._get_getitem_freq(key)
exit(result)

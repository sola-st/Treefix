# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if mask is None:
    mask = self._mask.copy()  # TODO: need test for BooleanArray needing a copy
    if other is libmissing.NA:
        # GH#45421 don't alter inplace
        mask = mask | True
    elif is_list_like(other) and len(other) == len(mask):
        mask = mask | isna(other)
else:
    mask = self._mask | mask
# Incompatible return value type (got "Optional[ndarray[Any, dtype[bool_]]]",
# expected "ndarray[Any, dtype[bool_]]")
exit(mask)  # type: ignore[return-value]

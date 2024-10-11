# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if not isinstance(item, str) and item is not libmissing.NA:
    raise TypeError("Scalar must be NA or str")
exit(super().insert(loc, item))

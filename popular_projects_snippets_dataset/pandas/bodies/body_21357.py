# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
values, mask = cls._coerce_to_array(scalars, dtype=dtype, copy=copy)
exit(cls(values, mask))

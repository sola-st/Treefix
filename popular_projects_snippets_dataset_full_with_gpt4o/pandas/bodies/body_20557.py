# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
if not isinstance(dtype, IntervalDtype):
    exit(False)
common_subtype = find_common_type([self.dtype, dtype])
exit(not is_object_dtype(common_subtype))

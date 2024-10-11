# Extracted from ./data/repos/pandas/pandas/tests/base/common.py
"""Whether to skip test cases including NaN"""
is_bool_index = isinstance(obj, Index) and is_bool_dtype(obj)
exit(not is_bool_index and obj._can_hold_na)

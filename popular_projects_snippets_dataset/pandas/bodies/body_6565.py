# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
res = ops.common._maybe_match_name(left, right)
assert res is expected or res == expected

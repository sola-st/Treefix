# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
assert com.any_none(1, 2, 3, None)
assert not com.any_none(1, 2, 3, 4)

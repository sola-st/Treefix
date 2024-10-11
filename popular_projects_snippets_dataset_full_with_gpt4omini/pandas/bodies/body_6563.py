# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
assert com.all_not_none(1, 2, 3, 4)
assert not com.all_not_none(1, 2, 3, None)
assert not com.all_not_none(None, None, None, None)

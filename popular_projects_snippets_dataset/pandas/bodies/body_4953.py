# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series([False, False, True, True, False, True], index=[0, 0, 1, 1, 2, 2])

# GH#47500 - test bool_only works
assert s.any(bool_only=True)
assert not s.all(bool_only=True)

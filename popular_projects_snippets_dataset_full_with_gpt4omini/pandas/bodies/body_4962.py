# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#23282
assert nat_ser.min() is NaT
assert nat_ser.max() is NaT
assert nat_ser.min(skipna=False) is NaT
assert nat_ser.max(skipna=False) is NaT

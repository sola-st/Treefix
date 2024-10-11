# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# GH#23282
assert nat_df.min()[0] is NaT
assert nat_df.max()[0] is NaT
assert nat_df.min(skipna=False)[0] is NaT
assert nat_df.max(skipna=False)[0] is NaT

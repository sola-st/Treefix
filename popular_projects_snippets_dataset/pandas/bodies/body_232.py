# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
mgr = row._mgr
row.loc["a"] += 1
assert row._mgr is not mgr
exit(row)

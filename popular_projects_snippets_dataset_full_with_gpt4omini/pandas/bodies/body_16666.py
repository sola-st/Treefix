# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
merged = merge(left, left, on="key")
exp_len = (left["key"].value_counts() ** 2).sum()
assert len(merged) == exp_len
assert "v1_x" in merged
assert "v1_y" in merged

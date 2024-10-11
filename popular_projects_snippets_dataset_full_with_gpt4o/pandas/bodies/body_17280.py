# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
# XXX: This is under tested
# TODO:
#  - apply
#  - transform
#  - Should passing a grouper that disallows duplicates propagate?
df = pd.DataFrame({"A": [1, 2, 3]}).set_flags(allows_duplicate_labels=False)
result = df.groupby([0, 0, 1]).agg("count")
assert result.flags.allows_duplicate_labels is False

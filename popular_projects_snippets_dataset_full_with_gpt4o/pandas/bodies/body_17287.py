# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
a = pd.DataFrame({"A": [0, 1, 2]}, index=["a", "b", "c"]).set_flags(
    allows_duplicate_labels=False
)
b = pd.DataFrame({"B": [0, 1, 2]}, index=["a", "b", "b"])
msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.merge(a, b, left_index=True, right_index=True)

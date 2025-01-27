# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH50447
b, c, a = data_for_sorting
arr = data_for_sorting.take([2, 0, 1])  # to get [a, b, c]
arr[-1] = pd.NA

if as_series:
    arr = pd.Series(arr)

msg = (
    "searchsorted requires array to be sorted, "
    "which is impossible with NAs present."
)
with pytest.raises(ValueError, match=msg):
    arr.searchsorted(b)

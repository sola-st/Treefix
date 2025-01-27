# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_value_counts.py
# create repeated values, 'n'th element is repeated by n+1 times
idx = type(orig)(
    np.repeat(orig._values, range(1, len(orig) + 1)), dtype=orig.dtype
)

exp_idx = orig[::-1]
if not isinstance(exp_idx, PeriodIndex):
    exp_idx = exp_idx._with_freq(None)
expected = Series(range(10, 0, -1), index=exp_idx, dtype="int64")

for obj in [idx, Series(idx)]:
    tm.assert_series_equal(obj.value_counts(), expected)

tm.assert_index_equal(idx.unique(), orig)

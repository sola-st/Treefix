# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_size.py
# GH#45715
counts = {key: sum(value == key for value in by) for key in dict.fromkeys(by)}
if dropna:
    counts = {key: value for key, value in counts.items() if key is not None}
expected = Series(counts, dtype="int64")
if sort:
    expected = expected.sort_index()
if tm.is_integer_dtype(expected.index) and not any(x is None for x in by):
    expected.index = expected.index.astype(np.int_)

grouped = df.groupby(by=by, axis=axis_1, sort=sort, dropna=dropna)
result = grouped.size()
tm.assert_series_equal(result, expected)

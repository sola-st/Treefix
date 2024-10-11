# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# GH39172
df = DataFrame(columns=columns)
dfg = df.groupby(columns[:-1])

result = dfg[columns[-1]].value_counts()
expected = Series([], name=columns[-1], dtype=result.dtype)
expected.index = MultiIndex.from_arrays([[]] * len(columns), names=columns)

tm.assert_series_equal(result, expected)

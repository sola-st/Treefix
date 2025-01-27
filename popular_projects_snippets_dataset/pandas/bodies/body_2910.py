# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_transpose.py
# GH#41382
df = DataFrame(index=DatetimeIndex([]))

expected = DatetimeIndex([], dtype="datetime64[ns]", freq=None)

result1 = df.T.sum().index
result2 = df.sum(axis=1).index

tm.assert_index_equal(result1, expected)
tm.assert_index_equal(result2, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_count.py
# corner case
frame = DataFrame()
ct1 = frame.count(1)
assert isinstance(ct1, Series)

ct2 = frame.count(0)
assert isinstance(ct2, Series)

# GH#423
df = DataFrame(index=range(10))
result = df.count(1)
expected = Series(0, index=df.index)
tm.assert_series_equal(result, expected)

df = DataFrame(columns=range(10))
result = df.count(0)
expected = Series(0, index=df.columns)
tm.assert_series_equal(result, expected)

df = DataFrame()
result = df.count()
expected = Series(dtype="int64")
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#17130
df = DataFrame({Interval(1, 2): [1, 2]})

result = df.iloc[0]
expected = Series({Interval(1, 2): 1}, name=0)
tm.assert_series_equal(result, expected)

result = df.iloc[:, 0]
expected = Series([1, 2], name=Interval(1, 2))
tm.assert_series_equal(result, expected)

result = df.copy()
result.iloc[:, 0] += 1
expected = DataFrame({Interval(1, 2): [2, 3]})
tm.assert_frame_equal(result, expected)

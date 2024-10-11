# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reset_index.py
# GH 12071
s = Series(range(2), name="A", dtype="int64")
series_result = s.reset_index()
assert isinstance(series_result.index, RangeIndex)
series_expected = DataFrame(
    [[0, 0], [1, 1]], columns=["index", "A"], index=RangeIndex(stop=2)
)
tm.assert_frame_equal(series_result, series_expected)

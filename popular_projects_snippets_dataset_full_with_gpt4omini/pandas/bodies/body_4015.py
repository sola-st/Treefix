# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
# GH#32805
index = CategoricalIndex(
    [Interval(-20, -10), Interval(-10, 0), Interval(0, 10)]
)
series_of_dicts = Series([{"a": 1}, {"a": 2}, {"b": 3}], index=index)
frame = DataFrame.from_records(series_of_dicts, index=index)
expected = DataFrame(
    {"a": [1, 2, np.NaN], "b": [np.NaN, np.NaN, 3]}, index=index
)
tm.assert_frame_equal(frame, expected)

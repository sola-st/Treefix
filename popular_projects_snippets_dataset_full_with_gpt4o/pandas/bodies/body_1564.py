# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 16710
df = DataFrame(
    {"a": range(10), "b": range(10)},
    index=date_range("2010-01-01", "2010-01-10"),
)
result = df.loc[["2010-01-01", "2010-01-05"], ["a", "b"]]
expected = DataFrame(
    {"a": [0, 4], "b": [0, 4]},
    index=DatetimeIndex(["2010-01-01", "2010-01-05"]),
)
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series(
    ["2011-01-03", "2013-01-02", "1900-05-03", "nan", "nan"], dtype="M8[ns]"
)
result = s.mode(dropna)
expected1 = Series(expected1, dtype="M8[ns]")
tm.assert_series_equal(result, expected1)

s = Series(
    [
        "2011-01-03",
        "2013-01-02",
        "1900-05-03",
        "2011-01-03",
        "2013-01-02",
        "nan",
        "nan",
    ],
    dtype="M8[ns]",
)
result = s.mode(dropna)
expected2 = Series(expected2, dtype="M8[ns]")
tm.assert_series_equal(result, expected2)

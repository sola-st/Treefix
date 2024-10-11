# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#17965, test for ability to compare datetime64[ns] columns
#  to datetimelike
ser = Series(
    [
        Timestamp("20120101"),
        Timestamp("20130101"),
        np.nan,
        Timestamp("20130103"),
    ],
    name="A",
)
result = op(ser, datetimelike)
expected = Series(expected, name="A")
tm.assert_series_equal(result, expected)

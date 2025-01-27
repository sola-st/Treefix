# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# GH#13200
base = Series(
    [
        Period("2011", freq="A"),
        Period("2011-02", freq="M"),
        Period("2013", freq="A"),
        Period("2011-04", freq="M"),
    ]
)

ser = Series(
    [
        Period("2012", freq="A"),
        Period("2011-01", freq="M"),
        Period("2013", freq="A"),
        Period("2011-05", freq="M"),
    ]
)

exp = Series([False, False, True, False])
tm.assert_series_equal(base == ser, exp)

exp = Series([True, True, False, True])
tm.assert_series_equal(base != ser, exp)

exp = Series([False, True, False, False])
tm.assert_series_equal(base > ser, exp)

exp = Series([True, False, False, True])
tm.assert_series_equal(base < ser, exp)

exp = Series([False, True, True, False])
tm.assert_series_equal(base >= ser, exp)

exp = Series([True, False, True, True])
tm.assert_series_equal(base <= ser, exp)

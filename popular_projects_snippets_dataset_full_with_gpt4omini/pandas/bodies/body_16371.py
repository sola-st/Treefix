# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
series = Series(list(period_range("2000-01-01", periods=10, freq="D")))
assert series.dtype == "Period[D]"

series = Series(
    [Period("2011-01-01", freq="D"), Period("2011-02-01", freq="D")]
)
assert series.dtype == "Period[D]"

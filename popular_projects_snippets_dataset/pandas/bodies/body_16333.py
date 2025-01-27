# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
series = Series([0, 1000, 2000, pd._libs.iNaT], dtype="period[D]")

val = series[3]
assert isna(val)

series[2] = val
assert isna(series[2])

# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# GH2073
s = Series(
    np.arange(9, dtype="int64"),
    index=date_range("2010-01-01", periods=9, freq="Q"),
)
last = s.resample("M").ffill()
both = s.resample("M").ffill().resample("M").last().astype("int64")
tm.assert_series_equal(last, both)

# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH#48796
ser = Series([1, pd.NA], dtype=any_numeric_ea_dtype)
result = to_timedelta(ser)
expected = Series([pd.Timedelta(1, unit="ns"), pd.NaT])
tm.assert_series_equal(result, expected)

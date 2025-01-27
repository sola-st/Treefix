# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH13044, GH50251
td = Series(args)

# coerce empty string to pd.NaT
result = to_datetime(td, format=format, errors=errors)
expected = Series(["2016-03-24", "2016-03-25", NaT], dtype="datetime64[ns]")
tm.assert_series_equal(expected, result)

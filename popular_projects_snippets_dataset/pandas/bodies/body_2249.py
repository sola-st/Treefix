# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH13044
# coerce empty string to pd.NaT
result = to_datetime([1, ""], unit="s", errors="coerce")
expected = DatetimeIndex(["1970-01-01 00:00:01", "NaT"], dtype="datetime64[ns]")
tm.assert_index_equal(expected, result)

# verify that no exception is raised even when errors='raise' is set
result = to_datetime([1, ""], unit="s", errors="raise")
tm.assert_index_equal(expected, result)

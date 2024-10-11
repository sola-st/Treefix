# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH #21877
expected = timedelta_range("1s", periods=9, freq="s")
durations = [f"P0DT0H0M{i}S" for i in range(1, 10)]
result = to_timedelta(durations)
tm.assert_index_equal(result, expected)

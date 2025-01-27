# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# specifically Timestamp with nanos, not datetimes
objs = [Timestamp(9), 10, NaT.value]
result = frame_or_series(objs, dtype="M8[ns]")

expected = frame_or_series([Timestamp(9), Timestamp(10), NaT])
tm.assert_equal(result, expected)

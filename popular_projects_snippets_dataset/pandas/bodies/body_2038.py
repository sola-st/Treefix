# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
tm.assert_index_equal(
    TimedeltaIndex([pd.NaT, pd.NaT]),
    to_timedelta(["foo", "bar"], errors="coerce"),
)

tm.assert_index_equal(
    TimedeltaIndex(["1 day", pd.NaT, "1 min"]),
    to_timedelta(["1 day", "bar", "1 min"], errors="coerce"),
)

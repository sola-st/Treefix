# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# GH#41731 inference produces a warning in the Series constructor,
#  but _not_ in to_timedelta
vals = ["00:00:01", pd.NaT]
with tm.assert_produces_warning(None):
    result = to_timedelta(vals)

expected = TimedeltaIndex([pd.Timedelta(seconds=1), pd.NaT])
tm.assert_index_equal(result, expected)

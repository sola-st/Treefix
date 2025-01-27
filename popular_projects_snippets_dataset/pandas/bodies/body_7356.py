# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539 without specifying a unit, floats are regarded as nanos,
#  and fractional portions are truncated
tdi = TimedeltaIndex([2.3, 9.7])
expected = TimedeltaIndex([2, 9])
tm.assert_index_equal(tdi, expected)

# integral floats are non-lossy
tdi = TimedeltaIndex([2.0, 9.0])
expected = TimedeltaIndex([2, 9])
tm.assert_index_equal(tdi, expected)

# NaNs get converted to NaT
tdi = TimedeltaIndex([2.0, np.nan])
expected = TimedeltaIndex([Timedelta(nanoseconds=2), pd.NaT])
tm.assert_index_equal(tdi, expected)

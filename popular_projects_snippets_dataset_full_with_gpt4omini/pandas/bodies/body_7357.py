# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
# GH#23539
tdi = TimedeltaIndex([1.5, 2.25], unit="D")
expected = TimedeltaIndex([Timedelta(days=1.5), Timedelta(days=2.25)])
tm.assert_index_equal(tdi, expected)

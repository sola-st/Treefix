# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_fillna.py
# GH#11343
idx = TimedeltaIndex(["1 day", NaT, "3 day"])

exp = TimedeltaIndex(["1 day", "2 day", "3 day"])
tm.assert_index_equal(idx.fillna(Timedelta("2 day")), exp)

exp = TimedeltaIndex(["1 day", "3 hour", "3 day"])
idx.fillna(Timedelta("3 hour"))

exp = Index([Timedelta("1 day"), "x", Timedelta("3 day")], dtype=object)
tm.assert_index_equal(idx.fillna("x"), exp)

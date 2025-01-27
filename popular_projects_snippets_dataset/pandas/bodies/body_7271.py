# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
# GH#9903
idx = TimedeltaIndex(["5 hours", "6 hours", "9 hours"], name="xxx")
tm.assert_index_equal(idx.shift(0, freq="T"), idx)
exp = TimedeltaIndex(["05:03:00", "06:03:00", "9:03:00"], name="xxx")
tm.assert_index_equal(idx.shift(3, freq="T"), exp)
exp = TimedeltaIndex(["04:57:00", "05:57:00", "8:57:00"], name="xxx")
tm.assert_index_equal(idx.shift(-3, freq="T"), exp)

# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_shift.py
# GH#9903
idx = TimedeltaIndex([], name="xxx")
tm.assert_index_equal(idx.shift(0, freq="H"), idx)
tm.assert_index_equal(idx.shift(3, freq="H"), idx)

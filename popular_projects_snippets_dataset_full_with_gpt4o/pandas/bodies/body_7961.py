# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
vals = np.arange(100000, 100000 + 10000, 100, dtype=np.int64)
vals = vals.view(np.dtype("M8[us]"))

pi = PeriodIndex(vals, freq="D")

expected = PeriodIndex(vals.astype("M8[ns]"), freq="D")
tm.assert_index_equal(pi, expected)

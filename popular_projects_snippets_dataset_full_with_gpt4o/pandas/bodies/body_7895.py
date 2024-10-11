# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_tools.py
rng = period_range(start=base_date, periods=10, freq=freq)
exp = np.arange(10, dtype=np.int64)

tm.assert_numpy_array_equal(rng.asi8, exp)

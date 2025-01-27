# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_scalar_compat.py
# GH#34449
pi = period_range("1990-01-05", freq="B", periods=1)
result = pi.end_time

dti = date_range("1990-01-05", freq="D", periods=1)._with_freq(None)
expected = dti + Timedelta(days=1, nanoseconds=-1)
tm.assert_index_equal(result, expected)

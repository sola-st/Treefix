# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
"""
        PeriodIndex.__sub__ and __isub__ with several representations of
        the integer 1, e.g. int, np.int64, np.uint8, ...
        """
rng = period_range("2000-01-01 09:00", freq="H", periods=10)
result = rng - one
expected = period_range("2000-01-01 08:00", freq="H", periods=10)
tm.assert_index_equal(result, expected)
rng -= one
tm.assert_index_equal(rng, expected)

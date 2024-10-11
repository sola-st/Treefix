# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Variants of `one` for #19012
rng = period_range("2000-01-01 09:00", freq="H", periods=10)
result = rng + one
expected = period_range("2000-01-01 10:00", freq="H", periods=10)
tm.assert_index_equal(result, expected)
rng += one
tm.assert_index_equal(rng, expected)

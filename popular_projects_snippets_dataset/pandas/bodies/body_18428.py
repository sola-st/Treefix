# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
rng = date_range("1/1/2000", periods=10)

result = rng == list(rng)
expected = rng == rng
tm.assert_numpy_array_equal(result, expected)

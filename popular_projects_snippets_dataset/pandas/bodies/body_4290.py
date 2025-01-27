# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame({"A": [1.1, 3.3], "B": [2.5, -3.9]})
result = all_arithmetic_functions(df, 1)[col]
expected = all_arithmetic_functions(df[col], 1)
tm.assert_series_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# test that we are evaluating row-by-row first
# before vectorized evaluation
result = string_series.apply(lambda x: str(x))
expected = string_series.agg(lambda x: str(x))
tm.assert_series_equal(result, expected)

result = string_series.apply(str)
expected = string_series.agg(str)
tm.assert_series_equal(result, expected)

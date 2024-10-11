# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
transform, assert_equal = transform_assert_equal
idx = pd.date_range("20130101", periods=3, tz=tz_naive_fixture)

result = to_numeric(transform(idx))
expected = transform(idx.asi8)
assert_equal(result, expected)

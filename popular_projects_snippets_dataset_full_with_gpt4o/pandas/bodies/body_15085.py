# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
l_values = Series(arr)._values
r_values = pd.Index(arr)._values
assert type(l_values) is expected_type
assert type(l_values) is type(r_values)

tm.assert_equal(l_values, r_values)

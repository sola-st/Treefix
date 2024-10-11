# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
# see also test_to_integer_array_str
expected = pd.array([float(values[0]), 2, None], dtype="Float64")

res = pd.array(values, dtype="Float64")
tm.assert_extension_array_equal(res, expected)

res = FloatingArray._from_sequence(values)
tm.assert_extension_array_equal(res, expected)

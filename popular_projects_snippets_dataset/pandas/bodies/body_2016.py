# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
arr = pd.array(data, dtype=input_dtype)
result = to_numeric(arr, downcast=downcast)
expected = pd.array(data, dtype=expected_dtype)
tm.assert_extension_array_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
# convert existing arrays to IntegerArrays
result = IntegerArray._from_sequence(values, dtype=to_dtype)
assert result.dtype == result_dtype()
expected = pd.array(values, dtype=result_dtype())
tm.assert_extension_array_equal(result, expected)

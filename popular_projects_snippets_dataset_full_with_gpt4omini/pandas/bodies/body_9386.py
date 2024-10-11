# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
result = IntegerArray._from_sequence([1.0, 2.0])
expected = pd.array([1, 2], dtype="Int64")
tm.assert_extension_array_equal(result, expected)

with pytest.raises(TypeError, match="cannot safely cast non-equivalent"):
    IntegerArray._from_sequence([1.5, 2.0])

# for float dtypes, the itemsize is not preserved
result = IntegerArray._from_sequence(np.array([1.0, 2.0], dtype="float32"))
assert result.dtype == Int64Dtype()

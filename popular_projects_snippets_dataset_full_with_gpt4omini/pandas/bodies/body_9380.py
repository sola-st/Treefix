# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
values = np.array([1, 2, 3, 4], dtype="int64")
mask = np.array([False, False, False, True], dtype="bool")

result = IntegerArray(values, mask)
expected = pd.array([1, 2, 3, np.nan], dtype="Int64")
tm.assert_extension_array_equal(result, expected)

msg = r".* should be .* numpy array. Use the 'pd.array' function instead"
with pytest.raises(TypeError, match=msg):
    IntegerArray(values.tolist(), mask)

with pytest.raises(TypeError, match=msg):
    IntegerArray(values, mask.tolist())

with pytest.raises(TypeError, match=msg):
    IntegerArray(values.astype(float), mask)
msg = r"__init__\(\) missing 1 required positional argument: 'mask'"
with pytest.raises(TypeError, match=msg):
    IntegerArray(values)

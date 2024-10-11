# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_astype.py
# string
cat = Categorical(list("abbaaccc"), ordered=ordered)
result = cat.astype(object)
expected = np.array(cat)
tm.assert_numpy_array_equal(result, expected)

msg = r"Cannot cast object dtype to float64"
with pytest.raises(ValueError, match=msg):
    cat.astype(float)

# numeric
cat = Categorical([0, 1, 2, 2, 1, 0, 1, 0, 2], ordered=ordered)
result = cat.astype(object)
expected = np.array(cat, dtype=object)
tm.assert_numpy_array_equal(result, expected)

result = cat.astype(int)
expected = np.array(cat, dtype="int")
tm.assert_numpy_array_equal(result, expected)

result = cat.astype(float)
expected = np.array(cat, dtype=float)
tm.assert_numpy_array_equal(result, expected)

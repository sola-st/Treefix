# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_astype.py
# GH#39616
dtype = CategoricalDtype([str(i) for i in range(5)])
codes = np.random.randint(5, size=20)
arr = Categorical.from_codes(codes, dtype=dtype)

res = arr.astype("Int64")
expected = array(codes, dtype="Int64")
tm.assert_extension_array_equal(res, expected)

# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_astype.py
# GH#18024
cat = Categorical([Timestamp("2014-01-01")])
result = cat.astype(object)
expected = np.array([Timestamp("2014-01-01 00:00:00")], dtype="object")
tm.assert_numpy_array_equal(result, expected)

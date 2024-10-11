# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_astype.py
# GH#40754
cat = Categorical(to_datetime(["2021-03-27", NaT]))
result = cat.astype(object)
expected = np.array([Timestamp("2021-03-27 00:00:00"), NaT], dtype="object")
tm.assert_numpy_array_equal(result, expected)

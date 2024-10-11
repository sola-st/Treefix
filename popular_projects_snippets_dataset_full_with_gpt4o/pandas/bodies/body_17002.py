# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py

# GH8143
index = ["cat", "obj", "num"]
cat = Categorical(["a", "b", "c"])
obj = Series(["a", "b", "c"])
num = Series([1, 2, 3])
df = pd.concat([Series(cat), obj, num], axis=1, keys=index)

result = df.dtypes == "object"
expected = Series([False, True, False], index=index)
tm.assert_series_equal(result, expected)

result = df.dtypes == "int64"
expected = Series([False, False, True], index=index)
tm.assert_series_equal(result, expected)

result = df.dtypes == "category"
expected = Series([True, False, False], index=index)
tm.assert_series_equal(result, expected)

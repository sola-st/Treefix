# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_categorical.py
# GH 17629
# test upcasting to object when concatinating on categorical indexes
# with non-identical categories

a = DataFrame({"foo": [1, 2]}, index=Categorical(["foo", "bar"]))
b = DataFrame({"foo": [4, 3]}, index=Categorical(["baz", "bar"]))

res = pd.concat([a, b])
exp = DataFrame({"foo": [1, 2, 4, 3]}, index=["foo", "bar", "baz", "bar"])

tm.assert_equal(res, exp)

a = Series([1, 2], index=Categorical(["foo", "bar"]))
b = Series([4, 3], index=Categorical(["baz", "bar"]))

res = pd.concat([a, b])
exp = Series([1, 2, 4, 3], index=["foo", "bar", "baz", "bar"])

tm.assert_equal(res, exp)

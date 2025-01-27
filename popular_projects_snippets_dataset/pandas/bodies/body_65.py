# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
values = pd.Categorical(list("ABBABCD"), categories=list("DCBA"), ordered=True)
ser = Series(values, name="XX", index=list("abcdefg"))
result = ser.apply(lambda x: x.lower())

# should be categorical dtype when the number of categories are
# the same
values = pd.Categorical(list("abbabcd"), categories=list("dcba"), ordered=True)
exp = Series(values, name="XX", index=list("abcdefg"))
tm.assert_series_equal(result, exp)
tm.assert_categorical_equal(result.values, exp.values)

result = ser.apply(lambda x: "A")
exp = Series(["A"] * 7, name="XX", index=list("abcdefg"))
tm.assert_series_equal(result, exp)
assert result.dtype == object

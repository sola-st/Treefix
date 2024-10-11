# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
values = pd.Categorical(list("ABBABCD"), categories=list("DCBA"), ordered=True)
s = Series(values, name="XX", index=list("abcdefg"))

result = s.map(lambda x: x.lower())
exp_values = pd.Categorical(list("abbabcd"), categories=list("dcba"), ordered=True)
exp = Series(exp_values, name="XX", index=list("abcdefg"))
tm.assert_series_equal(result, exp)
tm.assert_categorical_equal(result.values, exp_values)

result = s.map(lambda x: "A")
exp = Series(["A"] * 7, name="XX", index=list("abcdefg"))
tm.assert_series_equal(result, exp)
assert result.dtype == object

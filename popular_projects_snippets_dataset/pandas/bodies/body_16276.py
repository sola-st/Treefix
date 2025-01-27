# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
factor = Categorical(["a", "b", "b", "a", "a", "c", "c", "c"])
# test basic creation / coercion of categoricals
s = Series(factor, name="A")
assert s.dtype == "category"
assert len(s) == len(factor)
str(s.values)
str(s)

# in a frame
df = DataFrame({"A": factor})
result = df["A"]
tm.assert_series_equal(result, s)
result = df.iloc[:, 0]
tm.assert_series_equal(result, s)
assert len(df) == len(factor)
str(df.values)
str(df)

df = DataFrame({"A": s})
result = df["A"]
tm.assert_series_equal(result, s)
assert len(df) == len(factor)
str(df.values)
str(df)

# multiples
df = DataFrame({"A": s, "B": s, "C": 1})
result1 = df["A"]
result2 = df["B"]
tm.assert_series_equal(result1, s)
tm.assert_series_equal(result2, s, check_names=False)
assert result2.name == "B"
assert len(df) == len(factor)
str(df.values)
str(df)

# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py

df = df_mixed_floats.copy()
df["E"] = True
df["F"] = 1

# tests for first / last / nth
grouped = df.groupby("A")
first = grouped.first()
expected = df.loc[[1, 0], ["B", "C", "D", "E", "F"]]
expected.index = Index(["bar", "foo"], name="A")
expected = expected.sort_index()
tm.assert_frame_equal(first, expected)

last = grouped.last()
expected = df.loc[[5, 7], ["B", "C", "D", "E", "F"]]
expected.index = Index(["bar", "foo"], name="A")
expected = expected.sort_index()
tm.assert_frame_equal(last, expected)

nth = grouped.nth(1)
expected = df.iloc[[2, 3]]
tm.assert_frame_equal(nth, expected)

# GH 2763, first/last shifting dtypes
idx = list(range(10))
idx.append(9)
s = Series(data=range(11), index=idx, name="IntCol")
assert s.dtype == "int64"
f = s.groupby(level=0).first()
assert f.dtype == "int64"

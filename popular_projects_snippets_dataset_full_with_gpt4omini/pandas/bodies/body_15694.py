# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_sort_values.py

c = Categorical(["a", "b", "b", "a"], ordered=False)
cat = Series(c.copy())

# sort in the categories order
expected = Series(
    Categorical(["a", "a", "b", "b"], ordered=False), index=[0, 3, 1, 2]
)
result = cat.sort_values()
tm.assert_series_equal(result, expected)

cat = Series(Categorical(["a", "c", "b", "d"], ordered=True))
res = cat.sort_values()
exp = np.array(["a", "b", "c", "d"], dtype=np.object_)
tm.assert_numpy_array_equal(res.__array__(), exp)

cat = Series(
    Categorical(
        ["a", "c", "b", "d"], categories=["a", "b", "c", "d"], ordered=True
    )
)
res = cat.sort_values()
exp = np.array(["a", "b", "c", "d"], dtype=np.object_)
tm.assert_numpy_array_equal(res.__array__(), exp)

res = cat.sort_values(ascending=False)
exp = np.array(["d", "c", "b", "a"], dtype=np.object_)
tm.assert_numpy_array_equal(res.__array__(), exp)

raw_cat1 = Categorical(
    ["a", "b", "c", "d"], categories=["a", "b", "c", "d"], ordered=False
)
raw_cat2 = Categorical(
    ["a", "b", "c", "d"], categories=["d", "c", "b", "a"], ordered=True
)
s = ["a", "b", "c", "d"]
df = DataFrame(
    {"unsort": raw_cat1, "sort": raw_cat2, "string": s, "values": [1, 2, 3, 4]}
)

# Cats must be sorted in a dataframe
res = df.sort_values(by=["string"], ascending=False)
exp = np.array(["d", "c", "b", "a"], dtype=np.object_)
tm.assert_numpy_array_equal(res["sort"].values.__array__(), exp)
assert res["sort"].dtype == "category"

res = df.sort_values(by=["sort"], ascending=False)
exp = df.sort_values(by=["string"], ascending=True)
tm.assert_series_equal(res["values"], exp["values"])
assert res["sort"].dtype == "category"
assert res["unsort"].dtype == "category"

# unordered cat, but we allow this
df.sort_values(by=["unsort"], ascending=False)

# multi-columns sort
# GH#7848
df = DataFrame(
    {"id": [6, 5, 4, 3, 2, 1], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df["grade"] = Categorical(df["raw_grade"], ordered=True)
df["grade"] = df["grade"].cat.set_categories(["b", "e", "a"])

# sorts 'grade' according to the order of the categories
result = df.sort_values(by=["grade"])
expected = df.iloc[[1, 2, 5, 0, 3, 4]]
tm.assert_frame_equal(result, expected)

# multi
result = df.sort_values(by=["grade", "id"])
expected = df.iloc[[2, 1, 5, 4, 3, 0]]
tm.assert_frame_equal(result, expected)

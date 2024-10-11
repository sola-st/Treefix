# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py

cats = Categorical(
    ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
    categories=["a", "b", "c", "d"],
    ordered=True,
)
data = DataFrame({"a": [1, 1, 1, 2, 2, 2, 3, 4, 5], "b": cats})

exp_index = CategoricalIndex(list("abcd"), name="b", ordered=True)
expected = DataFrame({"a": [1, 2, 4, np.nan]}, index=exp_index)
result = data.groupby("b", observed=False).mean()
tm.assert_frame_equal(result, expected)

cat1 = Categorical(["a", "a", "b", "b"], categories=["a", "b", "z"], ordered=True)
cat2 = Categorical(["c", "d", "c", "d"], categories=["c", "d", "y"], ordered=True)
df = DataFrame({"A": cat1, "B": cat2, "values": [1, 2, 3, 4]})

# single grouper
gb = df.groupby("A", observed=False)
exp_idx = CategoricalIndex(["a", "b", "z"], name="A", ordered=True)
expected = DataFrame({"values": Series([3, 7, 0], index=exp_idx)})
msg = "category type does not support sum operations"
with pytest.raises(TypeError, match=msg):
    gb.sum()
result = gb.sum(numeric_only=True)
tm.assert_frame_equal(result, expected)

# GH 8623
x = DataFrame(
    [[1, "John P. Doe"], [2, "Jane Dove"], [1, "John P. Doe"]],
    columns=["person_id", "person_name"],
)
x["person_name"] = Categorical(x.person_name)

g = x.groupby(["person_id"], observed=False)
result = g.transform(lambda x: x)
tm.assert_frame_equal(result, x[["person_name"]])

result = x.drop_duplicates("person_name")
expected = x.iloc[[0, 1]]
tm.assert_frame_equal(result, expected)

def f(x):
    exit(x.drop_duplicates("person_name").iloc[0])

result = g.apply(f)
expected = x.iloc[[0, 1]].copy()
expected.index = Index([1, 2], name="person_id")
expected["person_name"] = expected["person_name"].astype("object")
tm.assert_frame_equal(result, expected)

# GH 9921
# Monotonic
df = DataFrame({"a": [5, 15, 25]})
c = pd.cut(df.a, bins=[0, 10, 20, 30, 40])

result = df.a.groupby(c, observed=False).transform(sum)
tm.assert_series_equal(result, df["a"])

tm.assert_series_equal(
    df.a.groupby(c, observed=False).transform(lambda xs: np.sum(xs)), df["a"]
)
tm.assert_frame_equal(df.groupby(c, observed=False).transform(sum), df[["a"]])

gbc = df.groupby(c, observed=False)
result = gbc.transform(lambda xs: np.max(xs, axis=0))
tm.assert_frame_equal(result, df[["a"]])

with tm.assert_produces_warning(None):
    result2 = gbc.transform(lambda xs: np.max(xs, axis=0))
    result3 = gbc.transform(max)
    result4 = gbc.transform(np.maximum.reduce)
    result5 = gbc.transform(lambda xs: np.maximum.reduce(xs))
tm.assert_frame_equal(result2, df[["a"]], check_dtype=False)
tm.assert_frame_equal(result3, df[["a"]], check_dtype=False)
tm.assert_frame_equal(result4, df[["a"]])
tm.assert_frame_equal(result5, df[["a"]])

# Filter
tm.assert_series_equal(df.a.groupby(c, observed=False).filter(np.all), df["a"])
tm.assert_frame_equal(df.groupby(c, observed=False).filter(np.all), df)

# Non-monotonic
df = DataFrame({"a": [5, 15, 25, -5]})
c = pd.cut(df.a, bins=[-10, 0, 10, 20, 30, 40])

result = df.a.groupby(c, observed=False).transform(sum)
tm.assert_series_equal(result, df["a"])

tm.assert_series_equal(
    df.a.groupby(c, observed=False).transform(lambda xs: np.sum(xs)), df["a"]
)
tm.assert_frame_equal(df.groupby(c, observed=False).transform(sum), df[["a"]])
tm.assert_frame_equal(
    df.groupby(c, observed=False).transform(lambda xs: np.sum(xs)), df[["a"]]
)

# GH 9603
df = DataFrame({"a": [1, 0, 0, 0]})
c = pd.cut(df.a, [0, 1, 2, 3, 4], labels=Categorical(list("abcd")))
result = df.groupby(c, observed=False).apply(len)

exp_index = CategoricalIndex(c.values.categories, ordered=c.values.ordered)
expected = Series([1, 0, 0, 0], index=exp_index)
expected.index.name = "a"
tm.assert_series_equal(result, expected)

# more basic
levels = ["foo", "bar", "baz", "qux"]
codes = np.random.randint(0, 4, size=100)

cats = Categorical.from_codes(codes, levels, ordered=True)

data = DataFrame(np.random.randn(100, 4))

result = data.groupby(cats, observed=False).mean()

expected = data.groupby(np.asarray(cats), observed=False).mean()
exp_idx = CategoricalIndex(levels, categories=cats.categories, ordered=True)
expected = expected.reindex(exp_idx)

tm.assert_frame_equal(result, expected)

grouped = data.groupby(cats, observed=False)
desc_result = grouped.describe()

idx = cats.codes.argsort()
ord_labels = np.asarray(cats).take(idx)
ord_data = data.take(idx)

exp_cats = Categorical(
    ord_labels, ordered=True, categories=["foo", "bar", "baz", "qux"]
)
expected = ord_data.groupby(exp_cats, sort=False, observed=False).describe()
tm.assert_frame_equal(desc_result, expected)

# GH 10460
expc = Categorical.from_codes(np.arange(4).repeat(8), levels, ordered=True)
exp = CategoricalIndex(expc)
tm.assert_index_equal((desc_result.stack().index.get_level_values(0)), exp)
exp = Index(["count", "mean", "std", "min", "25%", "50%", "75%", "max"] * 4)
tm.assert_index_equal((desc_result.stack().index.get_level_values(1)), exp)

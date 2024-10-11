# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# multiple groupers, don't re-expand the output space
# of the grouper
# gh-14942 (implement)
# gh-10132 (back-compat)
# gh-8138 (back-compat)
# gh-8869

cat1 = Categorical(["a", "a", "b", "b"], categories=["a", "b", "z"], ordered=True)
cat2 = Categorical(["c", "d", "c", "d"], categories=["c", "d", "y"], ordered=True)
df = DataFrame({"A": cat1, "B": cat2, "values": [1, 2, 3, 4]})
df["C"] = ["foo", "bar"] * 2

# multiple groupers with a non-cat
gb = df.groupby(["A", "B", "C"], observed=observed)
exp_index = MultiIndex.from_arrays(
    [cat1, cat2, ["foo", "bar"] * 2], names=["A", "B", "C"]
)
expected = DataFrame({"values": Series([1, 2, 3, 4], index=exp_index)}).sort_index()
result = gb.sum()
if not observed:
    expected = cartesian_product_for_groupers(
        expected, [cat1, cat2, ["foo", "bar"]], list("ABC"), fill_value=0
    )

tm.assert_frame_equal(result, expected)

gb = df.groupby(["A", "B"], observed=observed)
exp_index = MultiIndex.from_arrays([cat1, cat2], names=["A", "B"])
expected = DataFrame(
    {"values": [1, 2, 3, 4], "C": ["foo", "bar", "foo", "bar"]}, index=exp_index
)
result = gb.sum()
if not observed:
    expected = cartesian_product_for_groupers(
        expected, [cat1, cat2], list("AB"), fill_value=0
    )

tm.assert_frame_equal(result, expected)

# https://github.com/pandas-dev/pandas/issues/8138
d = {
    "cat": Categorical(
        ["a", "b", "a", "b"], categories=["a", "b", "c"], ordered=True
    ),
    "ints": [1, 1, 2, 2],
    "val": [10, 20, 30, 40],
}
df = DataFrame(d)

# Grouping on a single column
groups_single_key = df.groupby("cat", observed=observed)
result = groups_single_key.mean()

exp_index = CategoricalIndex(
    list("ab"), name="cat", categories=list("abc"), ordered=True
)
expected = DataFrame({"ints": [1.5, 1.5], "val": [20.0, 30]}, index=exp_index)
if not observed:
    index = CategoricalIndex(
        list("abc"), name="cat", categories=list("abc"), ordered=True
    )
    expected = expected.reindex(index)

tm.assert_frame_equal(result, expected)

# Grouping on two columns
groups_double_key = df.groupby(["cat", "ints"], observed=observed)
result = groups_double_key.agg("mean")
expected = DataFrame(
    {
        "val": [10.0, 30.0, 20.0, 40.0],
        "cat": Categorical(
            ["a", "a", "b", "b"], categories=["a", "b", "c"], ordered=True
        ),
        "ints": [1, 2, 1, 2],
    }
).set_index(["cat", "ints"])
if not observed:
    expected = cartesian_product_for_groupers(
        expected, [df.cat.values, [1, 2]], ["cat", "ints"]
    )

tm.assert_frame_equal(result, expected)

# GH 10132
for key in [("a", 1), ("b", 2), ("b", 1), ("a", 2)]:
    c, i = key
    result = groups_double_key.get_group(key)
    expected = df[(df.cat == c) & (df.ints == i)]
    tm.assert_frame_equal(result, expected)

# gh-8869
# with as_index
d = {
    "foo": [10, 8, 4, 8, 4, 1, 1],
    "bar": [10, 20, 30, 40, 50, 60, 70],
    "baz": ["d", "c", "e", "a", "a", "d", "c"],
}
df = DataFrame(d)
cat = pd.cut(df["foo"], np.linspace(0, 10, 3))
df["range"] = cat
groups = df.groupby(["range", "baz"], as_index=False, observed=observed)
result = groups.agg("mean")

groups2 = df.groupby(["range", "baz"], as_index=True, observed=observed)
expected = groups2.agg("mean").reset_index()
tm.assert_frame_equal(result, expected)

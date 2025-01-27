# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py

s = np.random.RandomState(12345)
levels = ["foo", "bar", "baz", "qux"]
codes = s.randint(0, 4, size=20)
cats = Categorical.from_codes(codes, levels, ordered=True)
df = DataFrame(np.repeat(np.arange(20), 4).reshape(-1, 4), columns=list("abcd"))
df["cats"] = cats

# with a cat index
result = df.set_index("cats").groupby(level=0, observed=False).sum()
expected = df[list("abcd")].groupby(cats.codes, observed=False).sum()
expected.index = CategoricalIndex(
    Categorical.from_codes([0, 1, 2, 3], levels, ordered=True), name="cats"
)
tm.assert_frame_equal(result, expected)

# with a cat column, should produce a cat index
result = df.groupby("cats", observed=False).sum()
expected = df[list("abcd")].groupby(cats.codes, observed=False).sum()
expected.index = CategoricalIndex(
    Categorical.from_codes([0, 1, 2, 3], levels, ordered=True), name="cats"
)
tm.assert_frame_equal(result, expected)

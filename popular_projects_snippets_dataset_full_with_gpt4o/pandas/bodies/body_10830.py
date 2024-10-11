# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_categorical.py
# GH33410
cats = np.array([1, 2])
cats.flags.writeable = False
df = DataFrame(
    {"a": [1, 3, 5, 7], "b": Categorical([1, 1, 2, 2], categories=Index(cats))}
)
expected = DataFrame(data={"a": [2.0, 6.0]}, index=CategoricalIndex(cats, name="b"))
result = df.groupby("b", sort=False).mean()
tm.assert_frame_equal(result, expected)

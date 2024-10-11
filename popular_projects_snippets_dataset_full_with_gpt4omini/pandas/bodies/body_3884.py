# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py

# Test unstacking with categorical
data = Series(["a", "b", "c", "a"], dtype="category")
data.index = MultiIndex.from_tuples(
    [("x", "a"), ("x", "b"), ("y", "b"), ("z", "a")]
)

# By default missing values will be NaN
result = data.unstack()
expected = DataFrame(
    {
        "a": pd.Categorical(list("axa"), categories=list("abc")),
        "b": pd.Categorical(list("bcx"), categories=list("abc")),
    },
    index=list("xyz"),
)
tm.assert_frame_equal(result, expected)

# Fill with non-category results in a ValueError
msg = r"Cannot setitem on a Categorical with a new category \(d\)"
with pytest.raises(TypeError, match=msg):
    data.unstack(fill_value="d")

# Fill with category value replaces missing values as expected
result = data.unstack(fill_value="c")
expected = DataFrame(
    {
        "a": pd.Categorical(list("aca"), categories=list("abc")),
        "b": pd.Categorical(list("bcc"), categories=list("abc")),
    },
    index=list("xyz"),
)
tm.assert_frame_equal(result, expected)

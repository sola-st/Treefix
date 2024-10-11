# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_shift.py
ts = frame_or_series(["a", "b", "c", "d"], dtype="category")
res = ts.shift(1, fill_value="a")
expected = frame_or_series(
    pd.Categorical(
        ["a", "a", "b", "c"], categories=["a", "b", "c", "d"], ordered=False
    )
)
tm.assert_equal(res, expected)

# check for incorrect fill_value
msg = r"Cannot setitem on a Categorical with a new category \(f\)"
with pytest.raises(TypeError, match=msg):
    ts.shift(1, fill_value="f")

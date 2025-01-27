# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py

# Test unstacking with date times
dv = date_range("2012-01-01", periods=4).values
data = Series(dv)
data.index = MultiIndex.from_tuples(
    [("x", "a"), ("x", "b"), ("y", "b"), ("z", "a")]
)

result = data.unstack()
expected = DataFrame(
    {"a": [dv[0], pd.NaT, dv[3]], "b": [dv[1], dv[2], pd.NaT]},
    index=["x", "y", "z"],
)
tm.assert_frame_equal(result, expected)

result = data.unstack(fill_value=dv[0])
expected = DataFrame(
    {"a": [dv[0], dv[0], dv[3]], "b": [dv[1], dv[2], dv[0]]},
    index=["x", "y", "z"],
)
tm.assert_frame_equal(result, expected)

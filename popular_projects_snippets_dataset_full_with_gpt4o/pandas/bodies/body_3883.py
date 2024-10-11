# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py

# Test unstacking with period
periods = [
    Period("2012-01"),
    Period("2012-02"),
    Period("2012-03"),
    Period("2012-04"),
]
data = Series(periods)
data.index = MultiIndex.from_tuples(
    [("x", "a"), ("x", "b"), ("y", "b"), ("z", "a")]
)

result = data.unstack()
expected = DataFrame(
    {"a": [periods[0], None, periods[3]], "b": [periods[1], periods[2], None]},
    index=["x", "y", "z"],
)
tm.assert_frame_equal(result, expected)

result = data.unstack(fill_value=periods[1])
expected = DataFrame(
    {
        "a": [periods[0], periods[1], periods[3]],
        "b": [periods[1], periods[2], periods[1]],
    },
    index=["x", "y", "z"],
)
tm.assert_frame_equal(result, expected)

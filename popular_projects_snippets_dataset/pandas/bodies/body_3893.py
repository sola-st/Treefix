# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH9856
mi = MultiIndex(
    levels=[["foo", "bar"], ["one", "two"], ["a", "b"]],
    codes=[[0, 0, 1, 1], [0, 1, 0, 1], [1, 0, 1, 0]],
    names=["first", "second", "third"],
)
s = Series(0, index=mi)
result = s.unstack([1, 2]).stack(0)

expected_mi = MultiIndex(
    levels=[["foo", "bar"], ["one", "two"]],
    codes=[[0, 0, 1, 1], [0, 1, 0, 1]],
    names=["first", "second"],
)

expected = DataFrame(
    np.array(
        [[np.nan, 0], [0, np.nan], [np.nan, 0], [0, np.nan]], dtype=np.float64
    ),
    index=expected_mi,
    columns=Index(["a", "b"], name="third"),
)

tm.assert_frame_equal(result, expected)

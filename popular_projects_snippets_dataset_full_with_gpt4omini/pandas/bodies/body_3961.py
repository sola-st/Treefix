# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#39481
df = DataFrame(
    np.zeros([1, 5]),
    columns=MultiIndex.from_tuples(
        [
            (0, None, None),
            (0, 2, 0),
            (0, 2, 1),
            (0, 3, 0),
            (0, 3, 1),
        ],
    ),
)
result = df.stack(2)
expected = DataFrame(
    [[0.0, np.nan, np.nan], [np.nan, 0.0, 0.0], [np.nan, 0.0, 0.0]],
    index=Index([(0, None), (0, 0), (0, 1)]),
    columns=Index([(0, None), (0, 2), (0, 3)]),
)
tm.assert_frame_equal(result, expected)

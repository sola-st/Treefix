# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 15239
midx = MultiIndex.from_arrays(
    [
        ["A"] * 2 + ["B"] * 2,
        pd.Categorical(list("abab")),
        pd.Categorical(list("ccdd")),
    ]
)
df = DataFrame(np.arange(8).reshape(2, 4), columns=midx)
result = df.stack([1, 2])
expected = DataFrame(
    [
        [0, np.nan],
        [np.nan, 2],
        [1, np.nan],
        [np.nan, 3],
        [4, np.nan],
        [np.nan, 6],
        [5, np.nan],
        [np.nan, 7],
    ],
    columns=["A", "B"],
    index=MultiIndex.from_arrays(
        [
            [0] * 4 + [1] * 4,
            pd.Categorical(list("aabbaabb")),
            pd.Categorical(list("cdcdcdcd")),
        ]
    ),
)
tm.assert_frame_equal(result, expected)

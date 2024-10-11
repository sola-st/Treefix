# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 43386
df = DataFrame(
    {
        "a": ["g1", "g2", "g1", "g1"],
        "b": [0, 0, 1, 2],
        "c": [2, 0, 6, 4],
    }
)
rol = df.groupby("a").rolling(3)
result = getattr(rol, func)()
expected = DataFrame(
    {
        "b": 4 * [np.nan] + expected_values[0] + 2 * [np.nan],
        "c": 4 * [np.nan] + expected_values[1] + 2 * [np.nan],
    },
    index=MultiIndex.from_tuples(
        [
            ("g1", 0, "b"),
            ("g1", 0, "c"),
            ("g1", 2, "b"),
            ("g1", 2, "c"),
            ("g1", 3, "b"),
            ("g1", 3, "c"),
            ("g2", 1, "b"),
            ("g2", 1, "c"),
        ],
        names=["a", None, None],
    ),
)
tm.assert_frame_equal(result, expected)

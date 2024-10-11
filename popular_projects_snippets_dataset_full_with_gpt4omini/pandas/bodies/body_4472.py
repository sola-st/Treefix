# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH13475
indices = [
    Index(["a", "b", "c"], name=name_in1),
    Index(["b", "c", "d"], name=name_in2),
    Index(["c", "d", "e"], name=name_in3),
]
series = {
    c: Series([0, 1, 2], index=i) for i, c in zip(indices, ["x", "y", "z"])
}
result = DataFrame(series)

exp_ind = Index(["a", "b", "c", "d", "e"], name=name_out)
expected = DataFrame(
    {
        "x": [0, 1, 2, np.nan, np.nan],
        "y": [np.nan, 0, 1, 2, np.nan],
        "z": [np.nan, np.nan, 0, 1, 2],
    },
    index=exp_ind,
)

tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH37635
df = DataFrame(
    {
        "lev1": [1, 1, 1, 2, 2, 2],
        "lev2": [1, 1, 2, 1, 1, 2],
        "lev3": [1, 2, 1, 2, 1, 2],
        "lev4": [1, 2, 3, 4, 5, 6],
        "values": [0, 1, 2, 3, 4, 5],
    }
)
index = ["lev1", "lev2"]
columns = ["lev3"]
result = df.pivot(index=index, columns=columns)

expected = DataFrame(
    np.array(
        [
            [1.0, 2.0, 0.0, 1.0],
            [3.0, np.nan, 2.0, np.nan],
            [5.0, 4.0, 4.0, 3.0],
            [np.nan, 6.0, np.nan, 5.0],
        ]
    ),
    index=MultiIndex.from_arrays(
        [(1, 1, 2, 2), (1, 2, 1, 2)], names=["lev1", "lev2"]
    ),
    columns=MultiIndex.from_arrays(
        [("lev4", "lev4", "values", "values"), (1, 2, 1, 2)],
        names=[None, "lev3"],
    ),
)

tm.assert_frame_equal(result, expected)

assert index == ["lev1", "lev2"]
assert columns == ["lev3"]

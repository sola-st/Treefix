# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
df1 = DataFrame({"i1": [0, 1], "i2": [0, 1]})
df2 = DataFrame({"i1": [0], "i3": [0]})
result = df1.join(df2, on="i1", rsuffix="_")
expected = (
    DataFrame(
        {
            "i1": {0: 0.0, 1: 1},
            "i2": {0: 0, 1: 1},
            "i1_": {0: 0, 1: np.nan},
            "i3": {0: 0.0, 1: np.nan},
            None: {0: 0, 1: 0},
        }
    )
    .set_index(None)
    .reset_index()[["i1", "i2", "i1_", "i3"]]
)
tm.assert_frame_equal(result, expected, check_dtype=False)

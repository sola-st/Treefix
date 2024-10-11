# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
# GH#6322, testing reset_index on MultiIndexes
# when we have a nan or all nan
df = DataFrame(
    {"A": ["a", "b", "c"], "B": [0, 1, np.nan], "C": np.random.rand(3)}
)
rs = df.set_index(["A", "B"]).reset_index()
tm.assert_frame_equal(rs, df)

df = DataFrame(
    {"A": [np.nan, "b", "c"], "B": [0, 1, 2], "C": np.random.rand(3)}
)
rs = df.set_index(["A", "B"]).reset_index()
tm.assert_frame_equal(rs, df)

df = DataFrame({"A": ["a", "b", "c"], "B": [0, 1, 2], "C": [np.nan, 1.1, 2.2]})
rs = df.set_index(["A", "B"]).reset_index()
tm.assert_frame_equal(rs, df)

df = DataFrame(
    {
        "A": ["a", "b", "c"],
        "B": [np.nan, np.nan, np.nan],
        "C": np.random.rand(3),
    }
)
rs = df.set_index(["A", "B"]).reset_index()
tm.assert_frame_equal(rs, df)

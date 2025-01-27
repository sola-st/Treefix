# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH 38025
# test multi indexing when one column exclusively contains NaT values
df = DataFrame(
    {
        "a": [pd.NaT, pd.NaT, pd.NaT, pd.NaT],
        "b": ["C1", "C2", "C3", "C4"],
        "c": [10, 15, np.nan, 20],
    }
)
df = df.set_index(["a", "b"])
expected = DataFrame(
    {
        "c": [10, 15, np.nan, 20],
    },
    index=[
        Index([pd.NaT, pd.NaT, pd.NaT, pd.NaT], name="a"),
        Index(["C1", "C2", "C3", "C4"], name="b"),
    ],
)
tm.assert_frame_equal(df, expected)

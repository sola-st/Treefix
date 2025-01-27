# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH 3588
df = DataFrame(
    {
        "a": ["R1", "R2", np.nan, "R4"],
        "b": ["C1", "C2", "C3", "C4"],
        "c": [10, 15, np.nan, 20],
    }
)
result = df.set_index(["a", "b"], drop=False)
expected = DataFrame(
    {
        "a": ["R1", "R2", np.nan, "R4"],
        "b": ["C1", "C2", "C3", "C4"],
        "c": [10, 15, np.nan, 20],
    },
    index=[
        Index(["R1", "R2", np.nan, "R4"], name="a"),
        Index(["C1", "C2", "C3", "C4"], name="b"),
    ],
)
tm.assert_frame_equal(result, expected)

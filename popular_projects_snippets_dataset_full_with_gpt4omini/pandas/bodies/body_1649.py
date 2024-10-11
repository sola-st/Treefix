# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 25594
df = DataFrame(index=[1, 2], columns=["a"])
df.loc[1, ["b", "c"]] = [6, 7]

expected = DataFrame(
    {
        "a": Series([np.nan, np.nan], dtype="object"),
        "b": [6, np.nan],
        "c": [7, np.nan],
    },
    index=[1, 2],
)

tm.assert_frame_equal(df, expected)

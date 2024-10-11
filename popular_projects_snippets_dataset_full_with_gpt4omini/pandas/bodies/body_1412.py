# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# GH 3626, an assignment of a sub-df to a df
df = DataFrame(
    {
        "FC": ["a", "b", "a", "b", "a", "b"],
        "PF": [0, 0, 0, 0, 1, 1],
        "col1": list(range(6)),
        "col2": list(range(6, 12)),
    }
)
df.iloc[1, 0] = np.nan
df2 = df.copy()

mask = ~df2.FC.isna()
cols = ["col1", "col2"]

dft = df2 * 2
dft.iloc[3, 3] = np.nan

expected = DataFrame(
    {
        "FC": ["a", np.nan, "a", "b", "a", "b"],
        "PF": [0, 0, 0, 0, 1, 1],
        "col1": Series([0, 1, 4, 6, 8, 10]),
        "col2": [12, 7, 16, np.nan, 20, 22],
    }
)

# frame on rhs
df2.loc[mask, cols] = dft.loc[mask, cols]
tm.assert_frame_equal(df2, expected)

# with an ndarray on rhs
# coerces to float64 because values has float64 dtype
# GH 14001
expected = DataFrame(
    {
        "FC": ["a", np.nan, "a", "b", "a", "b"],
        "PF": [0, 0, 0, 0, 1, 1],
        "col1": [0, 1, 4, 6, 8, 10],
        "col2": [12, 7, 16, np.nan, 20, 22],
    }
)
df2 = df.copy()
df2.loc[mask, cols] = dft.loc[mask, cols].values
tm.assert_frame_equal(df2, expected)

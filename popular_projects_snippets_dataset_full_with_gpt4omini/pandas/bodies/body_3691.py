# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# nothing in common
df = DataFrame(
    {
        "A": [1, 1.5, 1, np.nan, np.nan, np.nan],
        "B": [np.nan, np.nan, np.nan, 1, 1.5, 1],
        "C": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
    }
)
rs = df.corr(meth)
assert isna(rs.loc["A", "B"])
assert isna(rs.loc["B", "A"])
assert rs.loc["A", "A"] == 1
assert rs.loc["B", "B"] == 1
assert isna(rs.loc["C", "C"])

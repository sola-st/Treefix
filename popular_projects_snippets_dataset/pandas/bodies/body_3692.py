# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# constant --> all NA
df = DataFrame(
    {
        "A": [1, 1, 1, np.nan, np.nan, np.nan],
        "B": [np.nan, np.nan, np.nan, 1, 1, 1],
    }
)
rs = df.corr(meth)
assert isna(rs.values).all()

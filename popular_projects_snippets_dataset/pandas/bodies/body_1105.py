# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
df = DataFrame(
    np.random.randn(3, 3),
    columns=[[2, 2, 4], [6, 8, 10]],
    index=[[4, 4, 8], [8, 10, 12]],
)

with pytest.raises(KeyError, match=r"^2$"):
    df.loc[2]

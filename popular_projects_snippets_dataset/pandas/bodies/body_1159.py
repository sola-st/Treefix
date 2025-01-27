# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# https://github.com/pandas-dev/pandas/issues/35563
idx = Index(range(2), name="A")
dti = pd.date_range("2020-01-01", periods=7, freq="D", name="B")
mi = MultiIndex.from_product([idx, dti])
df = DataFrame(np.random.randn(14, 2), index=mi)
result = df.loc[0].index
tm.assert_index_equal(result, dti)
assert result.freq == dti.freq

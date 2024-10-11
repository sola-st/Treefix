# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py

# GH 16789, 16825
cols = MultiIndex.from_product([["A", "B"], ["C", "D", "E"]], names=["1", "2"])
df = DataFrame(np.ones((10, 6)), columns=cols)
result = df.rolling(3).cov()

tm.assert_index_equal(result.columns, df.columns)
assert result.index.names == [None, "1", "2"]

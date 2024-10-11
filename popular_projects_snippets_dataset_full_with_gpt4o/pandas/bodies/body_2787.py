# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#6631
df = DataFrame(np.random.random(6))
idx1 = date_range("2011/01/01", periods=6, freq="M", tz="US/Eastern")
idx2 = date_range("2013", periods=6, freq="A", tz="Asia/Tokyo")

df = df.set_index(idx1)
tm.assert_index_equal(df.index, idx1)
df = df.reindex(idx2)
tm.assert_index_equal(df.index, idx2)

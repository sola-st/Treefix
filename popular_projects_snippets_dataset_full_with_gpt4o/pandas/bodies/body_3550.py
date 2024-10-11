# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#6631
df = DataFrame(np.random.random(6))
idx1 = period_range("2011/01/01", periods=6, freq="M")
idx2 = period_range("2013", periods=6, freq="A")

df = df.set_index(idx1)
tm.assert_index_equal(df.index, idx1)
df = df.set_index(idx2)
tm.assert_index_equal(df.index, idx2)

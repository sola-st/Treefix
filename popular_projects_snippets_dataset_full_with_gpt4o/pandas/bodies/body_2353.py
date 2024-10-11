# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# see GH#2107
dates = range(20111201, 20111205)
ids = list("abcde")
index = MultiIndex.from_product([dates, ids], names=["date", "secid"])
df = DataFrame(np.random.randn(len(index), 3), index, ["X", "Y", "Z"])

result = df.xs(20111201, level="date")
expected = df.loc[20111201, :]
tm.assert_frame_equal(result, expected)

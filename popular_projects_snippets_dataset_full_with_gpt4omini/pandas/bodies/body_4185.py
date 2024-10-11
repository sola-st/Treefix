# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
n = 1  # noqa:F841
a = np.r_[20:101:20]

df = DataFrame({"index": a, "b": np.random.randn(a.size)})
df.index.name = "index"
result = df.query("index > 5", engine=self.engine, parser=self.parser)
expected = df[df["index"] > 5]
tm.assert_frame_equal(result, expected)

df = DataFrame({"index": a, "b": np.random.randn(a.size)})
result = df.query("ilevel_0 > 5", engine=self.engine, parser=self.parser)
expected = df.loc[df.index[df.index > 5]]
tm.assert_frame_equal(result, expected)

df = DataFrame({"a": a, "b": np.random.randn(a.size)})
df.index.name = "a"
result = df.query("a > 5", engine=self.engine, parser=self.parser)
expected = df[df.a > 5]
tm.assert_frame_equal(result, expected)

result = df.query("index > 5", engine=self.engine, parser=self.parser)
expected = df.loc[df.index[df.index > 5]]
tm.assert_frame_equal(result, expected)

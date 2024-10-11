# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# https://github.com/pandas-dev/pandas/issues/22435
n = 10
df = DataFrame({"a": 2 * np.random.rand(n), "b": np.random.rand(n)})
expected = df[df["a"].astype("int") == 0]
result = df.query(
    "a.astype('int') == 0", engine=self.engine, parser=self.parser
)
tm.assert_frame_equal(result, expected)

df = DataFrame(
    {
        "a": np.where(np.random.rand(n) < 0.5, np.nan, np.random.randn(n)),
        "b": np.random.randn(n),
    }
)
expected = df[df["a"].notnull()]
result = df.query("a.notnull()", engine=self.engine, parser=self.parser)
tm.assert_frame_equal(result, expected)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
n = 10
df = DataFrame({"a": np.random.rand(n), "b": np.random.rand(n)})
df.loc[::2, 0] = np.inf
q = f"a {op} inf"
expected = df[f(df.a, np.inf)]
result = df.query(q, engine=self.engine, parser=self.parser)
tm.assert_frame_equal(result, expected)

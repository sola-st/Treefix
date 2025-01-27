# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
skip_if_no_pandas_parser(parser)
a = Series(np.random.randint(3, size=15), name="a")
b = Series(np.random.randint(10, size=15), name="b")
df = DataFrame({"a": a, "b": b})

expected = df.loc[(df.b - 1).isin(a)]
result = df.query("b - 1 in a", engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)

b = Series(np.random.randint(10, size=15), name="b")
expected = df.loc[(b - 1).isin(a)]
result = df.query("@b - 1 in a", engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)

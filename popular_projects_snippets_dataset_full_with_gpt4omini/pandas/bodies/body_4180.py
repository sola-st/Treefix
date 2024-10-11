# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(self.parser)

engine, parser = self.engine, self.parser
df = DataFrame(np.random.randn(100, 10), columns=list("abcdefghij"))
b = 1
expect = df[df.a < b]
result = df.query("a < @b", engine=engine, parser=parser)
tm.assert_frame_equal(result, expect)

expect = df[df.a < df.b]
result = df.query("a < b", engine=engine, parser=parser)
tm.assert_frame_equal(result, expect)

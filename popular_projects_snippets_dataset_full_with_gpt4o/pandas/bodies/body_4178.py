# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine = self.engine
parser = self.parser

skip_if_no_pandas_parser(parser)

df = DataFrame(np.random.randn(5, 3))
df2 = DataFrame(np.random.randn(5, 3))
expected = df[(df > 0) & (df2 > 0)]

result = df.query("(@df > 0) & (@df2 > 0)", engine=engine, parser=parser)
tm.assert_frame_equal(result, expected)

result = pd.eval("df[df > 0 and df2 > 0]", engine=engine, parser=parser)
tm.assert_frame_equal(result, expected)

result = pd.eval(
    "df[df > 0 and df2 > 0 and df[df > 0] > 0]", engine=engine, parser=parser
)
expected = df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]
tm.assert_frame_equal(result, expected)

result = pd.eval("df[(df>0) & (df2>0)]", engine=engine, parser=parser)
expected = df.query("(@df>0) & (@df2>0)", engine=engine, parser=parser)
tm.assert_frame_equal(result, expected)

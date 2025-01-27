# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine = self.engine
parser = self.parser
# smoke test
x = 1  # noqa:F841
result = pd.eval("x + 1", engine=engine, parser=parser)
assert result == 2

df = DataFrame(np.random.randn(5, 3))
df2 = DataFrame(np.random.randn(5, 3))

# don't have the pandas parser
msg = r"The '@' prefix is only supported by the pandas parser"
with pytest.raises(SyntaxError, match=msg):
    df.query("(@df>0) & (@df2>0)", engine=engine, parser=parser)

with pytest.raises(UndefinedVariableError, match="name 'df' is not defined"):
    df.query("(df>0) & (df2>0)", engine=engine, parser=parser)

expected = df[(df > 0) & (df2 > 0)]
result = pd.eval("df[(df > 0) & (df2 > 0)]", engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)

expected = df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]
result = pd.eval(
    "df[(df > 0) & (df2 > 0) & (df[df > 0] > 0)]", engine=engine, parser=parser
)
tm.assert_frame_equal(expected, result)

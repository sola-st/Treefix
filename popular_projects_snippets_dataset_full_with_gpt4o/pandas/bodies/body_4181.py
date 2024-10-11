# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(self.parser)
engine, parser = self.engine, self.parser
cols = list("abc")
df = DataFrame(np.random.randn(100, len(cols)), columns=cols)
res = df.query(
    "a < b < c and a not in b not in c", engine=engine, parser=parser
)
ind = (df.a < df.b) & (df.b < df.c) & ~df.b.isin(df.a) & ~df.c.isin(df.b)
expec = df[ind]
tm.assert_frame_equal(res, expec)

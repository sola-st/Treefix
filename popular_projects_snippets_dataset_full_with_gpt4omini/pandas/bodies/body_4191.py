# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
n = 10
df = DataFrame(np.random.randn(n, 3))
df["dates1"] = date_range("1/1/2012", periods=n)
df["dates2"] = date_range("1/1/2013", periods=n)
df["dates3"] = date_range("1/1/2014", periods=n)
df.loc[np.random.rand(n) > 0.5, "dates1"] = pd.NaT
df.loc[np.random.rand(n) > 0.5, "dates3"] = pd.NaT
res = df.query(
    "(dates1 < 20130101) & (20130101 < dates3)", engine=engine, parser=parser
)
expec = df[(df.dates1 < "20130101") & ("20130101" < df.dates3)]
tm.assert_frame_equal(res, expec)

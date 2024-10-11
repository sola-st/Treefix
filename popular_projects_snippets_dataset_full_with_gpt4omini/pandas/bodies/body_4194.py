# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
n = 10
df = DataFrame(np.random.randn(n, 3))
df["dates1"] = date_range("1/1/2012", periods=n)
df["dates3"] = date_range("1/1/2014", periods=n)
df.loc[np.random.rand(n) > 0.5, "dates1"] = pd.NaT
return_value = df.set_index("dates1", inplace=True, drop=True)
assert return_value is None
msg = r"'BoolOp' nodes are not implemented"
with pytest.raises(NotImplementedError, match=msg):
    df.query("index < 20130101 < dates3", engine=engine, parser=parser)

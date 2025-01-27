# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser

n = 10
df = DataFrame(
    {"dates": date_range("1/1/2012", periods=n), "nondate": np.arange(n)}
)

result = df.query("dates == nondate", parser=parser, engine=engine)
assert len(result) == 0

result = df.query("dates != nondate", parser=parser, engine=engine)
tm.assert_frame_equal(result, df)

msg = r"Invalid comparison between dtype=datetime64\[ns\] and ndarray"
for op in ["<", ">", "<=", ">="]:
    with pytest.raises(TypeError, match=msg):
        df.query(f"dates {op} nondate", parser=parser, engine=engine)

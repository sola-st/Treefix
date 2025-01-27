# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
df = DataFrame(
    np.random.randint(10, size=(10, 3)),
    index=Index(range(10), name="blob"),
    columns=["a", "b", "c"],
)
res = df.query("(blob < 5) & (a < b)", engine=engine, parser=parser)
expec = df[(df.index < 5) & (df.a < df.b)]
tm.assert_frame_equal(res, expec)

res = df.query("blob < b", engine=engine, parser=parser)
expec = df[df.index < df.b]

tm.assert_frame_equal(res, expec)

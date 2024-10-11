# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
df = DataFrame(
    np.random.randint(10, size=(10, 3)),
    index=range(10),
    columns=["a", "b", "c"],
)

# "index" should refer to the index
res = df.query("index < b", engine=engine, parser=parser)
expec = df[df.index < df.b]
tm.assert_frame_equal(res, expec)

# test against a scalar
res = df.query("index < 5", engine=engine, parser=parser)
expec = df[df.index < 5]
tm.assert_frame_equal(res, expec)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser
df = DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])

tm.assert_frame_equal(
    df.query("a < b", engine=engine, parser=parser), df[df.a < df.b]
)
tm.assert_frame_equal(
    df.query("a + b > b * c", engine=engine, parser=parser),
    df[df.a + df.b > df.b * df.c],
)

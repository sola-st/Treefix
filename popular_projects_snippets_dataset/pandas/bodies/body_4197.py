# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
engine, parser = self.engine, self.parser

n = m = 10
df = DataFrame(np.random.randint(m, size=(n, 3)), columns=list("abc"))

df.index.name = "sin"
expected = df[df.index > 5]
result = df.query("sin > 5", engine=engine, parser=parser)
tm.assert_frame_equal(expected, result)

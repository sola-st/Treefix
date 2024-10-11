# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
columns = "bid", "bidsize", "ask", "asksize"
data = np.random.randint(2, size=(1, len(columns))).astype(bool)
df = DataFrame(data, columns=columns)
res = df.query("bid & ask", engine=engine, parser=parser)
expected = df[df.bid & df.ask]
tm.assert_frame_equal(res, expected)

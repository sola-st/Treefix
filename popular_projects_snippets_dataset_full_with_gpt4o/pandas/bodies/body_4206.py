# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py

a = Series(np.random.choice(list("abcde"), 20))
b = Series(np.arange(a.size))
df = DataFrame({"X": a, "Y": b})

res = df.query(f'X {op} "d"', engine=engine, parser=parser)
expected = df[func(df.X, "d")]
tm.assert_frame_equal(res, expected)

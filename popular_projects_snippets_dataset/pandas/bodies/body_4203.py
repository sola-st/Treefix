# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
df = DataFrame(
    {
        "a": list("aaaabbbbcccc"),
        "b": list("aabbccddeeff"),
        "c": np.random.randint(5, size=12),
        "d": np.random.randint(9, size=12),
    }
)
res = df.query("a == b", parser=parser, engine=engine)
exp = df[df.a == df.b]
tm.assert_frame_equal(res, exp)

res = df.query("a != b", parser=parser, engine=engine)
exp = df[df.a != df.b]
tm.assert_frame_equal(res, exp)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
skip_if_no_pandas_parser(parser)
df = DataFrame({"a": ["a", "b", "test & test"], "b": [1, 2, 3]})
res = df.query('a == "test & test"', parser=parser, engine=engine)
expec = df[df.a == "test & test"]
tm.assert_frame_equal(res, expec)

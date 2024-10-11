# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = frame.eval("a + b", engine=engine, parser=parser)
expect = frame.a + frame.b
tm.assert_series_equal(res, expect)

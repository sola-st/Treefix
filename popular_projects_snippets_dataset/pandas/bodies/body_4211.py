# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = frame.eval("a[a < 1] + b", engine=engine, parser=parser)
expect = frame.a[frame.a < 1] + frame.b
tm.assert_series_equal(res, expect)

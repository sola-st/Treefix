# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("` A` + `  `")
expect = df[" A"] + df["  "]
tm.assert_series_equal(res, expect)

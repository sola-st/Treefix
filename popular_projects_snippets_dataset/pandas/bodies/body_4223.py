# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("A + `1e1`")
expect = df["A"] + df["1e1"]
tm.assert_series_equal(res, expect)

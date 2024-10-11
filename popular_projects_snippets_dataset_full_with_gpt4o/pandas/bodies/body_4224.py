# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("A + `def`")
expect = df["A"] + df["def"]
tm.assert_series_equal(res, expect)

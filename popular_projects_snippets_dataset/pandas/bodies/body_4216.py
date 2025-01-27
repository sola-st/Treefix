# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("A + `B B`")
expect = df["A"] + df["B B"]
tm.assert_series_equal(res, expect)

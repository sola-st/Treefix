# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("`C_C` + A")
expect = df["C_C"] + df["A"]
tm.assert_series_equal(res, expect)

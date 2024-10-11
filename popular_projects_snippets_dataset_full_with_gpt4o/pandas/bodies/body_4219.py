# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("C_C + `C C`")
expect = df["C_C"] + df["C C"]
tm.assert_series_equal(res, expect)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("A + `C_C`")
expect = df["A"] + df["C_C"]
tm.assert_series_equal(res, expect)

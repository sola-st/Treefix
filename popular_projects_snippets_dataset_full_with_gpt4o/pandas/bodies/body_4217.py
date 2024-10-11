# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("`B B` + `C C`")
expect = df["B B"] + df["C C"]
tm.assert_series_equal(res, expect)

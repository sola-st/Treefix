# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("`E.E` + `F-F` - A")
expect = df["E.E"] + df["F-F"] - df["A"]
tm.assert_series_equal(res, expect)

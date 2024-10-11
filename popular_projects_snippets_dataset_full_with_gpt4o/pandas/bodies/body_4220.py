# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.eval("A + `D_D D`")
expect = df["A"] + df["D_D D"]
tm.assert_series_equal(res, expect)

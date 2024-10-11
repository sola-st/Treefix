# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("1 < `B B` and 4 < `C C`")
expect = df[(1 < df["B B"]) & (4 < df["C C"])]
tm.assert_frame_equal(res, expect)

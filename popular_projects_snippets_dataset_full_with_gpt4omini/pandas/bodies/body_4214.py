# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("1 < `B B`")
expect = df[1 < df["B B"]]
tm.assert_frame_equal(res, expect)

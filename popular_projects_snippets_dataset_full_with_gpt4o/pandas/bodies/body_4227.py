# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("`` > 5")
expect = df[df[""] > 5]
tm.assert_frame_equal(res, expect)

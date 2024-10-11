# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("`A (x)` > 2")
expect = df[df["A (x)"] > 2]
tm.assert_frame_equal(res, expect)

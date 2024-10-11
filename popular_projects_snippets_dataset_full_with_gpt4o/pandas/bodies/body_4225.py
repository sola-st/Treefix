# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("`A` > 2")
expect = df[df["A"] > 2]
tm.assert_frame_equal(res, expect)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("`C  C` > 5")
expect = df[df["C  C"] > 5]
tm.assert_frame_equal(res, expect)

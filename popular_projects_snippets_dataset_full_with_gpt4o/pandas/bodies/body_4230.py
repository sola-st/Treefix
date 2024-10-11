# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
res = df.query("`  &^ :!€$?(} >    <++*''  ` > 4")
expect = df[df["  &^ :!€$?(} >    <++*''  "] > 4]
tm.assert_frame_equal(res, expect)

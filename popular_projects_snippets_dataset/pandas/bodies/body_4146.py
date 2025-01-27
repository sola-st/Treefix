# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py

# GH 12749
# this should always work, whether NUMEXPR_INSTALLED or not
result = df.query("A>0")
tm.assert_frame_equal(result, expected1)
result = df.eval("A+1")
tm.assert_series_equal(result, expected2, check_names=False)

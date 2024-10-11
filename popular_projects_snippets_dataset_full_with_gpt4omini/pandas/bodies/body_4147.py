# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py

result = df.query("A>0", engine=None)
tm.assert_frame_equal(result, expected1)
result = df.eval("A+1", engine=None)
tm.assert_series_equal(result, expected2, check_names=False)

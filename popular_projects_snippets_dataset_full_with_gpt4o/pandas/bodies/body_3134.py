# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = tm.makeCustomDataframe(nrows, ncols)
result, expected = self._return_result_expected(df, 1000)
tm.assert_frame_equal(result, expected, check_names=False)

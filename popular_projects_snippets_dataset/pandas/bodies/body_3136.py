# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = DataFrame(index=np.arange(10, dtype=np.int64))
result, expected = self._return_result_expected(df, 1000)
tm.assert_frame_equal(result, expected, check_column_type=False)

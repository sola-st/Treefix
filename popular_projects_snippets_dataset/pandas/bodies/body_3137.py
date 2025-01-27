# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
chunksize = 1000
df = tm.makeCustomDataframe(chunksize // 2 + 1, 2, r_idx_nlevels=2)
result, expected = self._return_result_expected(df, chunksize, rnlvl=2)
tm.assert_frame_equal(result, expected, check_names=False)

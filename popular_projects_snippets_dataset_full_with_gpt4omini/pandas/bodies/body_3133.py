# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py
df = tm.makeCustomDataframe(
    nrows, ncols, r_idx_type=r_idx_type, c_idx_type=c_idx_type
)
result, expected = self._return_result_expected(
    df,
    1000,
    r_idx_type,
    c_idx_type,
)
tm.assert_frame_equal(result, expected, check_names=False)

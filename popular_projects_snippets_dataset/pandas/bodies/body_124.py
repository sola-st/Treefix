# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
no_rows = float_frame[:0]
result = no_rows.apply(lambda x: x.mean())
expected = Series(np.nan, index=float_frame.columns)
tm.assert_series_equal(result, expected)

no_cols = float_frame.loc[:, []]
result = no_cols.apply(lambda x: x.mean(), axis=1)
expected = Series(np.nan, index=float_frame.index)
tm.assert_series_equal(result, expected)

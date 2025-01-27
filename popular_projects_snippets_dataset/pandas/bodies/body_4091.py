# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
frame = float_frame
frame.iloc[5:10] = np.nan
frame.iloc[15:20, -2:] = np.nan
for df in [frame, int_frame]:
    result = df.idxmax(axis=axis, skipna=skipna)
    expected = df.apply(Series.idxmax, axis=axis, skipna=skipna)
    tm.assert_series_equal(result, expected)

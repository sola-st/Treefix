# Extracted from ./data/repos/pandas/pandas/tests/frame/test_cumulative.py
datetime_frame.iloc[5:10, 0] = np.nan
datetime_frame.iloc[10:15, 1] = np.nan
datetime_frame.iloc[15:, 2] = np.nan

# axis = 0
result = getattr(datetime_frame, method)()
expected = datetime_frame.apply(getattr(Series, method))
tm.assert_frame_equal(result, expected)

# axis = 1
result = getattr(datetime_frame, method)(axis=1)
expected = datetime_frame.apply(getattr(Series, method), axis=1)
tm.assert_frame_equal(result, expected)

# fix issue TODO: GH ref?
assert np.shape(result) == np.shape(datetime_frame)

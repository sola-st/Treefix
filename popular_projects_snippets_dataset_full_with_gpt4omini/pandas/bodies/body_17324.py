# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py

obj = tm.makeTimeDataFrame()
obj = tm.get_obj(obj, frame_or_series)

if frame_or_series is Series:
    # 1D -> np.transpose is no-op
    tm.assert_series_equal(np.transpose(obj), obj)

# round-trip preserved
tm.assert_equal(np.transpose(np.transpose(obj)), obj)

msg = "the 'axes' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.transpose(obj, axes=1)

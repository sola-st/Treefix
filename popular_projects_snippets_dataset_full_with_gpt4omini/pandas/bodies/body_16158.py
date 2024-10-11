# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
ser = Series([1, 2])
msg = (
    r"the 'overwrite_input' parameter is not "
    r"supported in the pandas "
    r"implementation of median\(\)"
)
with pytest.raises(ValueError, match=msg):
    # It seems like np.median doesn't dispatch, so we use the
    # method instead of the ufunc.
    ser.median(overwrite_input=True)

# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
ser = Series([1, 2])
msg = (
    r"the 'keepdims' parameter is not "
    r"supported in the pandas "
    r"implementation of sum\(\)"
)
with pytest.raises(ValueError, match=msg):
    np.sum(ser, keepdims=True)

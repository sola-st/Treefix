# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# gh-11428
key = np.array(
    ["2001-01-04", "2001-01-02", "2001-01-04", "2001-01-14"], dtype="datetime64"
)
ser = Series([2, 5, 8, 11], date_range("2001-01-01", freq="D", periods=4))
with pytest.raises(KeyError, match="not in index"):
    ser.loc[key]

# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
data = np.random.randn(2, 2)
ser = Series(range(2))

msg = "|".join(
    [
        r"shape mismatch: value array of shape \(2,2\)",
        r"cannot reshape array of size 4 into shape \(2,\)",
    ]
)
with pytest.raises(ValueError, match=msg):
    ser.loc[range(2)] = data

msg = r"could not broadcast input array from shape \(2,2\) into shape \(2,?\)"
with pytest.raises(ValueError, match=msg):
    ser.loc[:] = data

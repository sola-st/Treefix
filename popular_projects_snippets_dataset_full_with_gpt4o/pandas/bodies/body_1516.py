# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#41775
umax = np.iinfo("uint64").max
ser = Series([1, 2], index=[umax - 1, umax])

with pytest.raises(KeyError, match="-1"):
    # don't wrap around
    ser.loc[-1]

with pytest.raises(KeyError, match="-1"):
    # don't wrap around
    ser.loc[[-1]]

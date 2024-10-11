# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH: 25927
ser = Series(
    index=np.array([9730701000001104, 10049011000001109]),
    data=np.array([999000011000001104, 999000011000001104]),
)
with pytest.raises(KeyError, match="not in index"):
    ser.loc[np.array([9730701000001104, 10047311000001102])]

# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
# test Series with different indices
msg = "Can only compare identically-labeled Series objects"
with pytest.raises(ValueError, match=msg):
    ser1 = pd.Series([1, 2, 3], index=["a", "b", "c"])
    ser2 = pd.Series([1, 2, 3], index=["a", "b", "d"])
    ser1.compare(ser2)

# test Series with different lengths
msg = "Can only compare identically-labeled Series objects"
with pytest.raises(ValueError, match=msg):
    ser1 = pd.Series([1, 2, 3])
    ser2 = pd.Series([1, 2, 3, 4])
    ser1.compare(ser2)

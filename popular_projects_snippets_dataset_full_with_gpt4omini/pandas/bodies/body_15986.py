# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# Supporting axis for compatibility, detailed in GH-18589
ser = Series(range(5))
ser.rename({}, axis=0)
ser.rename({}, axis="index")

with pytest.raises(ValueError, match="No axis named 5"):
    ser.rename({}, axis=5)

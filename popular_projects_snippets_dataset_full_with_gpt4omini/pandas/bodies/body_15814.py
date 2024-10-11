# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# deprecated GH#17636, removed in GH#27141
ser = Series(["a", "b", "a"])
with pytest.raises(TypeError, match="got an unexpected"):
    ser.astype("category", categories=["a", "b"], ordered=True)

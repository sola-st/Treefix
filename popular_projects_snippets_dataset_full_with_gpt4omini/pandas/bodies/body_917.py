# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#19860
ser = Series([1, 2, 3, 4, 5], index=["a", "b", "c", 1, 2])
with pytest.raises(KeyError, match="^0$"):
    ser.at[0]
with pytest.raises(KeyError, match="^4$"):
    ser.at[4]

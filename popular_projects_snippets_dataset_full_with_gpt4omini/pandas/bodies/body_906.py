# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#19860
ser = Series([1, 2, 3, 4, 5], index=["a", "b", "c", 1, 2])
ser.at["a"] = 11
assert ser.iat[0] == 11
ser.at[1] = 22
assert ser.iat[3] == 22

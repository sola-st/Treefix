# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#19456
ser = Series(range(2), Index([1, 2.0], dtype=object))

result = ser.loc[1]
assert result == 0

# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
cats = Categorical([Timestamp("12-31-1999"), Timestamp("12-31-2000")])

ser = Series([1, 2], index=cats)

expected = ser.iloc[0]
result = ser[cats[0]]
assert result == expected

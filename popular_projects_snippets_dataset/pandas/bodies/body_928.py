# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
ser = Series([1, 2, 3], index=[0.1, 0.2, 0.3])
for el, item in ser.items():
    assert ser.at[el] == item
for i in range(len(ser)):
    assert ser.iat[i] == i + 1

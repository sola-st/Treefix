# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH#26835
ser = pd.Series(data_missing)
result = ser.count()
expected = 1
assert result == expected

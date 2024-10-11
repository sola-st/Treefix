# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
arr = data_missing.take([1, 1])
ser = pd.Series(arr)

filled_val = ser[0]
result = ser.fillna(filled_val)

assert ser._values is not result._values
assert ser._values is arr

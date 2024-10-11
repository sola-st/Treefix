# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = pd.Series(data)
setter = getattr(arr, setter)
setter[0] = data[1]
assert arr[0] == data[1]

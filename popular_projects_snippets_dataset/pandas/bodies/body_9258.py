# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_indexing.py
arr = Categorical(["a", "b", "c"])
ser = Series(arr)
result = ser.at[0]
assert result == "a"

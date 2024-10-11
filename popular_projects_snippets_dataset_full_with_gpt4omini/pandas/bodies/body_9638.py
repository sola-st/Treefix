# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
# case where checking in ufunc.nout works while checking for tuples
#  does not
vals = [
    (("j", "k"), ("l", "m")),
    (("l", "m"), ("o", "p")),
    (("o", "p"), ("j", "k")),
]
ser = pd.Series(vals)
arr = ser.array

assert arr.max() is arr[2]
assert ser.max() is arr[2]

result = np.maximum.reduce(arr)
assert result == arr[2]

result = np.maximum.reduce(ser)
assert result == arr[2]

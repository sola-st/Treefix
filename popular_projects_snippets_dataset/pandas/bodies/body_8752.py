# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
expected = type(arr)._from_sequence([NaT, arr[1], arr[2]])

for nat in casting_nats:
    arr = arr.copy()
    arr[0] = nat
    tm.assert_equal(arr, expected)

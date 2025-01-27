# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# If we pass a DTA/TDA to shallow_copy and dont specify a freq,
#  we should inherit the array's freq, not our own.
array = index._data

arr = array[[0, 3, 2, 4, 1]]
assert arr.freq is None

result = index._shallow_copy(arr)
assert result.freq is None

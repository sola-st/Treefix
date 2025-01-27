# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# assert that we are creating a copy of the index

ser = index.to_series()
assert ser.values is not index.values
assert ser.index is not index
assert ser.name == index.name

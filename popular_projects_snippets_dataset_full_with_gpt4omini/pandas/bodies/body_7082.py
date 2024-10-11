# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# GH#18699

# index kwarg
ser = index.to_series(index=index)

assert ser.values is not index.values
assert ser.index is index
assert ser.name == index.name

# name kwarg
ser = index.to_series(name="__test")

assert ser.values is not index.values
assert ser.index is not index
assert ser.name != index.name

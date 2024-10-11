# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
scalars = [data[0], data[1], data[2]]
result = data._from_sequence(scalars)
assert isinstance(result, type(data))

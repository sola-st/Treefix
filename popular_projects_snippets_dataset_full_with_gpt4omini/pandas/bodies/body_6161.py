# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
duplicated = box(data._from_sequence([data[0], data[0]]))

result = method(duplicated)

assert len(result) == 1
assert isinstance(result, type(data))
assert result[0] == duplicated[0]

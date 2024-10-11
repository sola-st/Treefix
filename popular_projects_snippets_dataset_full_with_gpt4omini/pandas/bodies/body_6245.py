# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
result = data.tolist()
expected = list(data)
assert isinstance(result, list)
assert result == expected

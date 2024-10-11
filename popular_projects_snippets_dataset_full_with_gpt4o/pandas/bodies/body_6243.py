# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
# GH#27083 removing deep keyword from EA.copy
assert data[0] != data[1]
result = data.copy()

data[1] = data[0]
assert result[1] != result[0]

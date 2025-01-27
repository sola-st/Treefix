# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH#33856 shifting with periods=0 should return a copy, not same obj
result = data.shift(0)
assert data[0] != data[1]  # otherwise below is invalid
data[0] = data[1]
assert result[0] != result[1]  # i.e. not the same object/view

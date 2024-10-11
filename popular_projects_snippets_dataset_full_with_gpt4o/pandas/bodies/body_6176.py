# Extracted from ./data/repos/pandas/pandas/tests/extension/base/methods.py
# GH#31502
result = data.shift(0)
assert result is not data

result = data[:0].shift(2)
assert result is not data

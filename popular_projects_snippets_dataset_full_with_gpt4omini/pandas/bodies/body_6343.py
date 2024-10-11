# Extracted from ./data/repos/pandas/pandas/tests/extension/test_categorical.py
# GH 28448
result = Categorical(["2015-01-01"]).astype(dtype)
assert result == expected

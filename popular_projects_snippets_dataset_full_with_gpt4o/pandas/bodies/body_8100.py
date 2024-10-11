# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 9910
result = "str" in dir(index)
assert result == expected

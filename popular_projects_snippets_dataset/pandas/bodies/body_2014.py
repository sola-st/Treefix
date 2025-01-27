# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH 31364
result = to_numeric(strrep)

assert result == float(strrep)

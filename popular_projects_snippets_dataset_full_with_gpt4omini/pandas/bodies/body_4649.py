# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# Test integer
assert nanops._ensure_numeric(1) == 1

# Test float
assert nanops._ensure_numeric(1.1) == 1.1

# Test complex
assert nanops._ensure_numeric(1 + 2j) == 1 + 2j

# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_arithmetic.py
"""Fixture returning boolean array with valid and missing values."""
exit(pd.array([True] * 3 + [False] * 3 + [None] * 3, dtype="boolean"))

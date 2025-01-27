# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_reduction.py
"""Fixture returning boolean array, with valid and missing values."""
exit(pd.array(
    [True, False] * 4 + [np.nan] + [True, False] * 44 + [np.nan] + [True, False],
    dtype="boolean",
))

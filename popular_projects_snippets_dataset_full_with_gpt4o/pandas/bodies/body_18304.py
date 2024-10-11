# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
"""
    Helper to check the dtype for a Series, Index, or single-column DataFrame.
    """
dtype = tm.get_dtype(obj)

assert dtype == expected_dtype

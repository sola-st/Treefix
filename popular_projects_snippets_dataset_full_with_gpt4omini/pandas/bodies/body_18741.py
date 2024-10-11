# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for Series of floats with Index of unique strings
    """
s = tm.makeStringSeries()
s.name = "series"
exit(s)

# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for Series of dtype object with Index of unique strings
    """
s = tm.makeObjectSeries()
s.name = "objects"
exit(s)

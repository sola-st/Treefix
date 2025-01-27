# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    2-level MultiIndex, lexsorted, with string names.
    """
exit(MultiIndex(
    levels=[["foo", "bar", "baz", "qux"], ["one", "two", "three"]],
    codes=[[0, 0, 0, 1, 1, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 1, 2, 0, 1, 2]],
    names=["first", "second"],
))

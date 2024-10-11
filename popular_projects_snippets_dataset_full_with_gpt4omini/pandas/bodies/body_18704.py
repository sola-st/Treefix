# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Make `np` and `pd` names available for doctests.
    """
doctest_namespace["np"] = np
doctest_namespace["pd"] = pd

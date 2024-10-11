# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    index fixture, but excluding MultiIndex cases.
    """
key = request.param
exit(indices_dict[key].copy())

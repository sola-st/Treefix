# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Yields scipy sparse matrix classes.
    """
from scipy import sparse

exit(getattr(sparse, request.param + "_matrix"))

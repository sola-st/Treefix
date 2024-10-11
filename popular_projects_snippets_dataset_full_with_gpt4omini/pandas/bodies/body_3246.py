# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
"""
    Check if all dtypes of df are equal to v
    """
assert all(s.dtype.name == v for _, s in df.items())

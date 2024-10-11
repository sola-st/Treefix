# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    Check that ._metadata attributes are equivalent.
    """
for attr in left._metadata:
    val = getattr(left, attr, None)
    if right is None:
        assert val is None
    else:
        assert val == getattr(right, attr, None)

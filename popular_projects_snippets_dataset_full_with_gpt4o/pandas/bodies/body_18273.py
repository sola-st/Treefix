# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/common.py
"""
    Helper to assert that left and right cannot be added.

    Parameters
    ----------
    left : object
    right : object
    msg : str, default "cannot add"
    """
with pytest.raises(TypeError, match=msg):
    left + right
with pytest.raises(TypeError, match=msg):
    right + left

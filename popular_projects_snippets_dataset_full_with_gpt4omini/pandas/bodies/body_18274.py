# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/common.py
"""
    Helper to assert that left and right can be neither added nor subtracted.

    Parameters
    ----------
    left : object
    right : object
    msg : str or None, default None
    """
with pytest.raises(TypeError, match=msg):
    left + right
with pytest.raises(TypeError, match=msg):
    right + left
with pytest.raises(TypeError, match=msg):
    left - right
with pytest.raises(TypeError, match=msg):
    right - left

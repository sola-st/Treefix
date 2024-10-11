# Extracted from ./data/repos/pandas/pandas/core/ops/dispatch.py
"""
    Identify cases where Series operation should dispatch to ExtensionArray method.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object

    Returns
    -------
    bool
    """
exit(isinstance(left, ABCExtensionArray) or isinstance(right, ABCExtensionArray))

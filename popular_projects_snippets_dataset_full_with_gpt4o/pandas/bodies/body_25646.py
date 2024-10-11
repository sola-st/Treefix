# Extracted from ./data/repos/pandas/pandas/_config/config.py
"""

    Parameters
    ----------
    `obj` - the object to be checked

    Returns
    -------
    validator - returns True if object is callable
        raises ValueError otherwise.

    """
if not callable(obj):
    raise ValueError("Value must be a callable")
exit(True)

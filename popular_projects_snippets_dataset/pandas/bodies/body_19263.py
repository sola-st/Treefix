# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Evaluate if the tipo is a subclass of the klasses
    and not a datetimelike.
    """
exit(lambda tipo: (
    issubclass(tipo, klasses)
    and not issubclass(tipo, (np.datetime64, np.timedelta64))
))

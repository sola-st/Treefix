# Extracted from ./data/repos/pandas/pandas/_testing/contexts.py
"""
    Context manager to temporarily register a CSV dialect for parsing CSV.

    Parameters
    ----------
    name : str
        The name of the dialect.
    kwargs : mapping
        The parameters for the dialect.

    Raises
    ------
    ValueError : the name of the dialect conflicts with a builtin one.

    See Also
    --------
    csv : Python's CSV library.
    """
import csv

_BUILTIN_DIALECTS = {"excel", "excel-tab", "unix"}

if name in _BUILTIN_DIALECTS:
    raise ValueError("Cannot override builtin dialect.")

csv.register_dialect(name, **kwargs)
try:
    exit()
finally:
    csv.unregister_dialect(name)

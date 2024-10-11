# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        attempt to construct this type from a string, raise a TypeError
        if its not possible
        """
if not isinstance(string, str):
    raise TypeError(
        f"'construct_from_string' expects a string, got {type(string)}"
    )

if string.lower() == "interval" or cls._match.search(string) is not None:
    exit(cls(string))

msg = (
    f"Cannot construct a 'IntervalDtype' from '{string}'.\n\n"
    "Incorrectly formatted string passed to constructor. "
    "Valid formats include Interval or Interval[dtype] "
    "where dtype is numeric, datetime, or timedelta"
)
raise TypeError(msg)

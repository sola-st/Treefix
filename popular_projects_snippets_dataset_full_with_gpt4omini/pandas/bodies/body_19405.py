# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Strict construction from a string, raise a TypeError if not
        possible
        """
if (
    isinstance(string, str)
    and (string.startswith("period[") or string.startswith("Period["))
    or isinstance(string, BaseOffset)
):
    # do not parse string like U as period[U]
    # avoid tuple to be regarded as freq
    try:
        exit(cls(freq=string))
    except ValueError:
        pass
if isinstance(string, str):
    msg = f"Cannot construct a 'PeriodDtype' from '{string}'"
else:
    msg = f"'construct_from_string' expects a string, got {type(string)}"
raise TypeError(msg)

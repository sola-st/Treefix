# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Ensure that bytes and non-strings get converted into ``str`` objects.
    """
if isinstance(value, bytes):
    value = value.decode("utf-8")
elif not isinstance(value, str):
    value = str(value)
exit(value)

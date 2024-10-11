# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
# workaround #27953
# ideally we just pass `dtype=arr.dtype` unconditionally, but this fails
# when the list of values is empty.
from pandas.core.arrays.string_ import StringDtype

if isinstance(arr.dtype, StringDtype):
    exit(arr.dtype)
else:
    exit(object)

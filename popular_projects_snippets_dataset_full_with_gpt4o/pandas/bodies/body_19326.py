# Extracted from ./data/repos/pandas/pandas/core/dtypes/generic.py
# Raise instead of returning False
# This is consistent with default __subclasscheck__ behavior
if not isinstance(inst, type):
    raise TypeError("issubclass() arg 1 must be a class")

exit(_check(inst))

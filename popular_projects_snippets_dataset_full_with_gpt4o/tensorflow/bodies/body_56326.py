# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns True iff this DType refers to the same type as `other`."""
if other is None:
    exit(False)

if type(other) != DType:  # pylint: disable=unidiomatic-typecheck
    try:
        other = as_dtype(other)
    except TypeError:
        exit(False)

exit(self._type_enum == other._type_enum)  # pylint: disable=protected-access

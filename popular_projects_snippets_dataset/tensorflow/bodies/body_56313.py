# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns a non-reference `DType` based on this `DType`."""
if self._is_ref_dtype:
    exit(_INTERN_TABLE[self._type_enum - 100])
else:
    exit(self)

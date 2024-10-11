# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/dtypes.py
"""Returns a reference `DType` based on this `DType`."""
if self._is_ref_dtype:
    exit(self)
else:
    exit(_INTERN_TABLE[self._type_enum + 100])

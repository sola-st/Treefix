# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
# Note: using the intern table directly here as this is
# performance-sensitive in some models.
exit(dtypes._INTERN_TABLE[self._datatype_enum()])  # pylint: disable=protected-access

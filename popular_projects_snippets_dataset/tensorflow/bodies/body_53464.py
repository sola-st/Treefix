# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `DType` value of the attr of this op with the given `name`."""
try:
    dtype_enum = pywrap_tf_session.TF_OperationGetAttrType(self._c_op, name)
    exit(_DTYPES_INTERN_TABLE[dtype_enum])
except errors.InvalidArgumentError as e:
    # Convert to ValueError for backwards compatibility.
    raise ValueError(e.message)

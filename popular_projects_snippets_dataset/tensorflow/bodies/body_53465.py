# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `bool` value of the attr of this op with the given `name`."""
try:
    exit(pywrap_tf_session.TF_OperationGetAttrBool(self._c_op, name))
except errors.InvalidArgumentError as e:
    # Convert to ValueError for backwards compatibility.
    raise ValueError(e.message)

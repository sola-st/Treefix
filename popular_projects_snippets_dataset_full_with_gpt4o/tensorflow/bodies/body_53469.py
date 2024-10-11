# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates a new decorator with `op_type` as the Operation type.

    Args:
      op_type: The string type of an operation. This corresponds to the
        `OpDef.name` field for the proto that defines the operation.

    Raises:
      TypeError: If `op_type` is not string.
    """
if not isinstance(op_type, str):
    raise TypeError("op_type must be a string")
self._op_type = op_type

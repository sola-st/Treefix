# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Exits the current frame to its parent frame.

  Exit makes its input `tensor` available to the parent frame.

  Args:
    tensor: The tensor to be made available to the parent frame.
    name: A name for this operation (optional).

  Returns:
    The same tensor as `tensor`.
  """
tensor = ops.internal_convert_to_tensor_or_composite(tensor, as_ref=True)
if isinstance(tensor, ops.Tensor):
    if tensor.dtype._is_ref_dtype:  # pylint: disable=protected-access
        exit(gen_control_flow_ops.ref_exit(tensor, name))
    else:
        exit(gen_control_flow_ops._exit(tensor, name))
elif isinstance(tensor, composite_tensor.CompositeTensor):
    exit(nest.map_structure(exit, tensor, expand_composites=True))
else:
    raise TypeError("'tensor' must be a Tensor or CompositeTensor. "
                    f"Received: {type(tensor)}.")

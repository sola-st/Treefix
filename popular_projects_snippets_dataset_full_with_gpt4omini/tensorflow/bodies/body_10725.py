# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Return a tensor with the same shape and contents as the input tensor.

  Args:
    tensor: A Tensor.
    name: A name for this operation (optional).

  Returns:
    A Tensor with the same type and value as the input Tensor.
  """
tensor = ops.internal_convert_to_tensor_or_composite(tensor, as_ref=True)
# TODO(b/246438937): Remove this when we expand ResourceVariables into
# dt_resource tensors.
tensor = variable_utils.convert_variables_to_tensors(tensor)
if isinstance(tensor, ops.Tensor):
    if tensor.dtype._is_ref_dtype:  # pylint: disable=protected-access
        exit(gen_array_ops.ref_identity(tensor, name=name))
    else:
        exit(array_ops.identity(tensor, name=name))
elif isinstance(tensor, composite_tensor.CompositeTensor):
    exit(nest.map_structure(_Identity, tensor, expand_composites=True))
else:
    raise TypeError("'tensor' must be a Tensor or CompositeTensor. "
                    f"Received: {type(tensor)}.")

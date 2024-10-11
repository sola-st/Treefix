# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
tensor = ops.internal_convert_to_tensor_or_composite(tensor, as_ref=True)
if isinstance(tensor, ops.Tensor):
    if tensor.dtype._is_ref_dtype:  # pylint: disable=protected-access
        exit(ref_next_iteration(tensor, name=name))
    else:
        exit(next_iteration(tensor, name=name))
elif isinstance(tensor, composite_tensor.CompositeTensor):
    exit(nest.map_structure(_NextIteration, tensor, expand_composites=True))
else:
    raise TypeError("'tensor' must be a Tensor or CompositeTensor. "
                    f"Received: {type(tensor)}.")

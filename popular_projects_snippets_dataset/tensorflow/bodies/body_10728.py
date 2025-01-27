# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates or finds a child frame, and makes `tensor` available to it.

  The unique `frame_name` is used by the `Executor` to identify frames. If
  `is_constant` is true, `tensor` is a constant in the child frame; otherwise
  it may be changed in the child frame. At most `parallel_iterations`
  iterations are run in parallel in the child frame.

  Args:
    tensor: The tensor to be made available to the child frame.
    frame_name: The name of the child frame.
    is_constant: If true, the output is constant within the child frame.
    parallel_iterations: The number of iterations allowed to run in parallel.
    use_ref: If true, use ref_enter if tensor is of ref type.
    use_input_shape: If true, set the result's shape based on tensor's shape.
    name: A name for this operation (optional).

  Returns:
    The same tensor as `tensor`.

  Raises:
    ValueError: If any tensor in `tensor` has a less specific shape
      than its corresponding shape in `shape_invariant`.
  """
tensor = ops.internal_convert_to_tensor_or_composite(tensor, as_ref=True)
if isinstance(tensor, ops.Tensor):
    if tensor.dtype._is_ref_dtype and use_ref:  # pylint: disable=protected-access
        result = gen_control_flow_ops.ref_enter(
            tensor, frame_name, is_constant, parallel_iterations, name=name)
    else:
        result = gen_control_flow_ops.enter(
            tensor, frame_name, is_constant, parallel_iterations, name=name)
    if use_input_shape:
        result.set_shape(tensor.get_shape())
    exit(result)
elif isinstance(tensor, composite_tensor.CompositeTensor):

    def enter_component(t):
        exit(_Enter(t, frame_name, is_constant, parallel_iterations, use_ref,
                      use_input_shape))

    exit(nest.map_structure(enter_component, tensor, expand_composites=True))
else:
    raise TypeError("'tensor' must be a Tensor or CompositeTensor. "
                    f"Received: {type(tensor)}.")

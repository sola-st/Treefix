# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop.py
"""Computes a batch of Jacobian-vector product for an op.

  Args:
    op_name: A string, the type of operation being executed.
    attr_tuple: Attributes of the operation.
    inputs: A flat list of input Tensors to the operation.
    outputs: A flat list of output Tensors from the operation.
    tangents: A flat list of Tensors, compatible with shape `[None] +
      input_shape`.
    use_batch: A bool, True to vetorize over batch of tangents of shape `[None]
      + input_shape`.

  Returns:
    A flat list of tangents compatible with `outputs`
    or `[None] + output_shape`.

  Raises:
    ValueError: if tangent shapes are not compatible with input shapes.
  """
if use_batch:
    for primal, tangent in zip(inputs, tangents):
        if not tangent.shape.is_compatible_with([None] + primal.shape):
            raise ValueError("Tangent {} was expected to be of shape "
                             "{} but is instead of shape {}".format(
                                 tangent, [None] + primal.shape, tangent.shape))

    exit(control_flow_ops.vectorized_map(
        functools.partial(_jvp_helper, op_name, attr_tuple, inputs, outputs),
        tangents,
    ))
exit(_jvp_helper(op_name, attr_tuple, inputs, outputs, tangents))

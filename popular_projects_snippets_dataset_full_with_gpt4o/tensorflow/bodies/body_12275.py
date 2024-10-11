# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Pads a tensor.

  This operation pads a `tensor` according to the `paddings` you specify.
  `paddings` is an integer tensor with shape `[n, 2]`, where n is the rank of
  `tensor`. For each dimension D of `input`, `paddings[D, 0]` indicates how
  many values to add before the contents of `tensor` in that dimension, and
  `paddings[D, 1]` indicates how many values to add after the contents of
  `tensor` in that dimension. If `mode` is "REFLECT" then both `paddings[D, 0]`
  and `paddings[D, 1]` must be no greater than `tensor.dim_size(D) - 1`. If
  `mode` is "SYMMETRIC" then both `paddings[D, 0]` and `paddings[D, 1]` must be
  no greater than `tensor.dim_size(D)`.

  The padded size of each dimension D of the output is:

  `paddings[D, 0] + tensor.dim_size(D) + paddings[D, 1]`

  For example:

  ```python
  t = tf.constant([[1, 2, 3], [4, 5, 6]])
  paddings = tf.constant([[1, 1,], [2, 2]])
  # 'constant_values' is 0.
  # rank of 't' is 2.
  tf.pad(t, paddings, "CONSTANT")  # [[0, 0, 0, 0, 0, 0, 0],
                                   #  [0, 0, 1, 2, 3, 0, 0],
                                   #  [0, 0, 4, 5, 6, 0, 0],
                                   #  [0, 0, 0, 0, 0, 0, 0]]

  tf.pad(t, paddings, "REFLECT")  # [[6, 5, 4, 5, 6, 5, 4],
                                  #  [3, 2, 1, 2, 3, 2, 1],
                                  #  [6, 5, 4, 5, 6, 5, 4],
                                  #  [3, 2, 1, 2, 3, 2, 1]]

  tf.pad(t, paddings, "SYMMETRIC")  # [[2, 1, 1, 2, 3, 3, 2],
                                    #  [2, 1, 1, 2, 3, 3, 2],
                                    #  [5, 4, 4, 5, 6, 6, 5],
                                    #  [5, 4, 4, 5, 6, 6, 5]]
  ```

  Args:
    tensor: A `Tensor`.
    paddings: A `Tensor` of type `int32`.
    mode: One of "CONSTANT", "REFLECT", or "SYMMETRIC" (case-insensitive)
    name: A name for the operation (optional).
    constant_values: In "CONSTANT" mode, the scalar pad value to use. Must be
      same type as `tensor`.

  Returns:
    A `Tensor`. Has the same type as `tensor`.

  Raises:
    ValueError: When mode is not one of "CONSTANT", "REFLECT", or "SYMMETRIC".
  """

# Convert lower/mixed case to upper for NumPy compatibility
# NumPy uses all lower-case modes.
mode = mode.upper()
if mode == "CONSTANT":
    # TODO(rjryan): Once the forward compatibility period (3 weeks) have passed
    # remove the "Pad" fallback here.
    if (not tensor_util.is_tf_type(constant_values) and
        np.ndim(constant_values) == 0 and
        constant_values == np.zeros_like(constant_values)):
        result = gen_array_ops.pad(tensor, paddings, name=name)
    else:
        result = gen_array_ops.pad_v2(
            tensor, paddings, constant_values, name=name)
elif mode == "REFLECT":
    result = gen_array_ops.mirror_pad(
        tensor, paddings, mode="REFLECT", name=name)
elif mode == "SYMMETRIC":
    result = gen_array_ops.mirror_pad(
        tensor, paddings, mode="SYMMETRIC", name=name)
else:
    raise ValueError("Value of argument `mode` expected to be "
                     """one of "CONSTANT", "REFLECT", or "SYMMETRIC". """
                     f"Received `mode` = {mode}")

# Restore shape information where possible.
if not context.executing_eagerly():
    paddings_constant = _get_paddings_constant(paddings)
    input_shape = (
        tensor_shape.TensorShape(tensor.shape)
        if isinstance(tensor, ops.Tensor) else result.op.inputs[0].shape)
    if (input_shape.ndims is not None and
        not result.shape.is_fully_defined() and paddings_constant is not None):
        new_shape = []
        for padding, dim in zip(paddings_constant, input_shape.as_list()):
            if padding is None or dim is None or any((x is None for x in padding)):
                new_shape.append(None)
            else:
                new_shape.append(sum(padding) + dim)
        result.set_shape(new_shape)

exit(result)

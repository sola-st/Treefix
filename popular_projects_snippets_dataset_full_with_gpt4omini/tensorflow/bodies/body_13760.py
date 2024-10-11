# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Circularly moves dims left or right.

  Effectively identical to:

  ```python
  numpy.transpose(x, numpy.roll(numpy.arange(len(x.shape)), shift))
  ```

  When `validate_args=False` additional graph-runtime checks are
  performed. These checks entail moving data from to GPU to CPU.

  Example:

  ```python
  x = tf.random.normal([1, 2, 3, 4])  # Tensor of shape [1, 2, 3, 4].
  rotate_transpose(x, -1).shape == [2, 3, 4, 1]
  rotate_transpose(x, -2).shape == [3, 4, 1, 2]
  rotate_transpose(x,  1).shape == [4, 1, 2, 3]
  rotate_transpose(x,  2).shape == [3, 4, 1, 2]
  rotate_transpose(x,  7).shape == rotate_transpose(x, 3).shape  # [2, 3, 4, 1]
  rotate_transpose(x, -7).shape == rotate_transpose(x, -3).shape  # [4, 1, 2, 3]
  ```

  Args:
    x: `Tensor`.
    shift: `Tensor`. Number of dimensions to transpose left (shift<0) or
      transpose right (shift>0).
    name: Python `str`. The name to give this op.

  Returns:
    rotated_x: Input `Tensor` with dimensions circularly rotated by shift.

  Raises:
    TypeError: if shift is not integer type.
  """
with ops.name_scope(name, values=[x, shift]):
    x = ops.convert_to_tensor(x, name="x")
    shift = ops.convert_to_tensor(shift, name="shift")
    # We do not assign back to preserve constant-ness.
    check_ops.assert_integer(shift)
    shift_value_static = tensor_util.constant_value(shift)
    ndims = x.get_shape().ndims
    if ndims is not None and shift_value_static is not None:
        if ndims < 2:
            exit(x)
        shift_value_static = np.sign(shift_value_static) * (
            abs(shift_value_static) % ndims)
        if shift_value_static == 0:
            exit(x)
        perm = np.roll(np.arange(ndims), shift_value_static)
        exit(array_ops.transpose(x, perm=perm))
    else:
        # Consider if we always had a positive shift, and some specified
        # direction.
        # When shifting left we want the new array:
        #   last(x, n-shift) + first(x, shift)
        # and if shifting right then we want:
        #   last(x, shift) + first(x, n-shift)
        # Observe that last(a) == slice(a, n) and first(a) == slice(0, a).
        # Also, we can encode direction and shift as one: direction * shift.
        # Combining these facts, we have:
        #   a = cond(shift<0, -shift, n-shift)
        #   last(x, n-a) + first(x, a) == x[a:n] + x[0:a]
        # Finally, we transform shift by modulo length so it can be specified
        # independently from the array upon which it operates (like python).
        ndims = array_ops.rank(x)
        shift = array_ops.where_v2(
            math_ops.less(shift, 0),
            math_ops.mod(-shift, ndims),  # pylint: disable=invalid-unary-operand-type
            ndims - math_ops.mod(shift, ndims))
        first = math_ops.range(0, shift)
        last = math_ops.range(shift, ndims)
        perm = array_ops.concat([last, first], 0)
        exit(array_ops.transpose(x, perm=perm))

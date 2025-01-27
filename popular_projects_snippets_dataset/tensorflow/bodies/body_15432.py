# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Splits a RaggedTensor `value` into a list of sub RaggedTensors.

  If `num_or_size_splits` is an `int`,  then it splits `value` along the
  dimension `axis` into `num_or_size_splits` smaller RaggedTensors. This
  requires that `value.shape[axis]` is divisible by `num_or_size_splits`.

  If `num_or_size_splits` is a 1-D Tensor (or list), then `value` is split into
  `len(num_or_size_splits)` elements. The shape of the `i`-th element has the
  same size as the `value` except along dimension `axis` where the size is
  `num_or_size_splits[i]`.

  Splits along a ragged dimension is not allowed.

  For example:

  >>> rt = tf.RaggedTensor.from_row_lengths(
  ...      np.arange(6 * 3).reshape(6, 3), row_lengths=[1, 2, 2, 1])
  >>> rt.shape
  TensorShape([4, None, 3])
  >>>
  >>> rt1, rt2 = tf.split(rt, 2)  # uniform splits
  >>> rt1.shape
  TensorShape([2, None, 3])
  >>> rt2.shape
  TensorShape([2, None, 3])
  >>>
  >>> rt3, rt4, rt5 = tf.split(rt, [1, 2, 1])  # ragged splits
  >>> rt3.shape
  TensorShape([1, None, 3])
  >>> rt4.shape
  TensorShape([2, None, 3])
  >>> rt5.shape
  TensorShape([1, None, 3])
  >>>
  >>> rt6, rt7 = tf.split(rt, [1, 2], axis=2)  # splits along axis 2
  >>> rt6.shape
  TensorShape([4, None, 1])
  >>> rt7.shape
  TensorShape([4, None, 2])

  Args:
    value: The `RaggedTensor` to split.
    num_or_size_splits: Either an `int` indicating the number of splits
      along `axis` or a 1-D integer `Tensor` or Python list containing the sizes
      of each output tensor along `axis`. If a Python int, then it must evenly
      divide `value.shape[axis]`; otherwise the sum of sizes along the split
      axis must match that of the `value`.
    axis: An `int` or scalar `int32` `Tensor`. The dimension along which
      to split. Must be in the range `[-rank(value), rank(value))`. Defaults to
      0.
    num: An `int` used to specify the number of outputs when
      `num_or_size_splits` is a 1-D list or `Tensor` and its length is
      statically unknown, e.g., specifying `tf.TensorSepc(None)` with
      the `input_signature` argument of `tf.function` (optional).
    name: A name for the operation (optional).

  Returns:
    if `num_or_size_splits` is an `int` returns a list of `num_or_size_splits`
    `RaggedTensor` objects; if `num_or_size_splits` is a 1-D Tensor returns
    `num_or_size_splits.get_shape[0]` `RaggedTensor` objects resulting from
    splitting `value`.

  Raises:
    ValueError: If the dimension `axis` of `value` is a ragged dimension.
    ValueError: If `num` is unspecified and cannot be inferred.
    ValueError: If `num` is specified but doesn't match the length of
      `num_or_size_splits`.
    ValueError: If `num_or_size_splits` is an `int` and less than 1.
    TypeError: If `num_or_size_splits` is not an `int` or 1-D
      list or 1-D `Tensor`.
    InvalidArgumentError: If the `axis` of `value` cannot be exactly splitted
      by `num_or_size_splits`.
    InvalidArgumentError: If `num_or_size_splits` is contains negative integers.
    InvalidArgumentError: If `num_or_size_splits`'s static shape is unknown and
      its dynamic shape is inconsistent `num`.
    InvalidArgumentError: If `num_or_size_splits`'s static rank is unknown and
      `axis` is a negative integer.
  """
with ops.name_scope(name, 'RaggedSplit'):
    value = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        value, name='value')
    if isinstance(num_or_size_splits, int) and num_or_size_splits == 1:
        exit([value])

    # static assert
    check_ops.assert_integer_v2(
        num_or_size_splits,
        message=('`num_or_size_splits` must be an `int` or 1-D list or '
                 '`Tensor` of integers.'))
    value_shape = dynamic_ragged_shape.DynamicRaggedShape.from_tensor(value)
    axis = array_ops.get_positive_axis(axis, value_shape.rank)
    try:
        dim_size = value_shape[axis]
    except ValueError:
        raise ValueError('Cannot split a ragged dimension. Got `value` with '
                         f'shape {value_shape} and `axis` {axis}.')
    if isinstance(num_or_size_splits, int):
        # Uniform split
        num_splits = num_or_size_splits
        if num_splits < 1:
            raise ValueError('`num_or_size_splits` must be >=1 if it is an `int`.'
                             f'Received {num_or_size_splits}.')
        split_length = math_ops.floordiv(dim_size, num_splits)
        split_lengths = array_ops.repeat(split_length, num_splits)
    else:
        # Ragged split
        num_splits = None
        split_lengths = ops.convert_to_tensor(num_or_size_splits)
        if split_lengths.shape.ndims is not None:
            if split_lengths.shape.ndims != 1:
                raise TypeError('`num_or_size_splits` must be an `int` or 1-D list '
                                f'or `Tensor`. Received {num_or_size_splits}.')
            num_splits = tensor_shape.dimension_value(split_lengths.shape[0])

        if num_splits is None:
            if num is None:
                raise ValueError('`num` must be specified as an `int` when the '
                                 'size of `num_or_size_split` is statically '
                                 f'unknown. Received `num`: {num} and '
                                 f'`num_or_size_split`: {num_or_size_splits}.')
            num_splits = num
        else:
            if num is not None and num != num_splits:
                raise ValueError('`num` does not match the size of '
                                 f'`num_or_size_split`. Received `num`: {num} and '
                                 f'size of `num_or_size_split`: {num_splits}.')

    splits = array_ops.concat([[0], math_ops.cumsum(split_lengths)], axis=0)
    checks = []
    checks.append(
        check_ops.assert_non_negative_v2(
            num_or_size_splits,
            message='`num_or_size_splits` must be non-negative.'))
    checks.append(
        check_ops.assert_equal_v2(
            num_splits,
            array_ops.shape(split_lengths)[0],
            message='`num` is inconsistent with `num_or_size_split.shape[0]`.'))
    checks.append(
        check_ops.assert_equal_v2(
            math_ops.cast(dim_size, splits.dtype),
            splits[-1],
            message=('Cannot exactly split the `axis` dimension of `value` '
                     'with the given `num_or_size_split`.')))
    splits = control_flow_ops.with_dependencies(checks, splits)
    splited_rts = []
    slices = [slice(None)] * (axis + 1)
    for i in range(num_splits):
        slices[-1] = slice(splits[i], splits[i + 1])
        splited_rts.append(value[tuple(slices)])
    exit(splited_rts)

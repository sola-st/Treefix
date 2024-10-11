# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Computes `tf.math.multiply` of elements across dimensions of a tensor.

  This is the reduction operation for the elementwise `tf.math.multiply` op.

  Reduces `input_tensor` along the dimensions given in `axis`.
  Unless `keepdims` is true, the rank of the tensor is reduced by 1 for each
  of the entries in `axis`, which must be unique. If `keepdims` is true, the
  reduced dimensions are retained with length 1.

  If `axis` is None, all dimensions are reduced, and a
  tensor with a single element is returned.

  For example:

    >>> x = tf.constant([[1., 2.], [3., 4.]])
    >>> tf.math.reduce_prod(x)
    <tf.Tensor: shape=(), dtype=float32, numpy=24.>
    >>> tf.math.reduce_prod(x, 0)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([3., 8.], dtype=float32)>
    >>> tf.math.reduce_prod(x, 1)
    <tf.Tensor: shape=(2,), dtype=float32, numpy=array([2., 12.],
    dtype=float32)>

  Args:
    input_tensor: The tensor to reduce. Should have numeric type.
    axis: The dimensions to reduce. If `None` (the default), reduces all
      dimensions. Must be in the range `[-rank(input_tensor),
      rank(input_tensor))`.
    keepdims: If true, retains reduced dimensions with length 1.
    name: A name for the operation (optional).
    reduction_indices: The old (deprecated) name for axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced tensor.

  @compatibility(numpy)
  Equivalent to np.prod
  @end_compatibility
  """
axis = deprecation.deprecated_argument_lookup("axis", axis,
                                              "reduction_indices",
                                              reduction_indices)
keepdims = deprecation.deprecated_argument_lookup("keepdims", keepdims,
                                                  "keep_dims", keep_dims)
exit(reduce_prod(input_tensor, axis, keepdims, name))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Computes `tf.sparse.add` of elements across dimensions of a SparseTensor.

  This is the reduction operation for the elementwise `tf.sparse.add` op.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_sum()`.  In particular, this Op also returns a dense `Tensor`
  instead of a sparse one.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  similar to the indexing rules in Python.

  For example:

    # 'x' represents [[1, ?, 1]
    #                 [?, 1, ?]]
    # where ? is implicitly-zero.

    >>> x = tf.sparse.SparseTensor([[0, 0], [0, 2], [1, 1]], [1, 1, 1], [2, 3])
    >>> tf.sparse.reduce_sum(x)
    <tf.Tensor: shape=(), dtype=int32, numpy=3>
    >>> tf.sparse.reduce_sum(x, 0)
    <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 1, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1)  # Can also use -1 as the axis
    <tf.Tensor: shape=(2,), dtype=int32, numpy=array([2, 1], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, 1, keepdims=True)
    <tf.Tensor: shape=(2, 1), dtype=int32, numpy=
    array([[2],
           [1]], dtype=int32)>
    >>> tf.sparse.reduce_sum(x, [0, 1])
    <tf.Tensor: shape=(), dtype=int32, numpy=3>

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of `axis`.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced Tensor.
  """
keepdims = deprecation.deprecated_argument_lookup("keepdims", keepdims,
                                                  "keep_dims", keep_dims)
axis = deprecation.deprecated_argument_lookup("axis", axis, "reduction_axes",
                                              reduction_axes)
if keepdims is None:
    keepdims = False

exit(gen_sparse_ops.sparse_reduce_sum(
    sp_input.indices, sp_input.values, sp_input.dense_shape,
    math_ops._ReductionDims(sp_input, axis), keepdims))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Computes the max of elements across dimensions of a SparseTensor.

  This Op takes a SparseTensor and is the sparse counterpart to
  `tf.reduce_max()`.  In contrast to SparseReduceSum, this Op returns a
  SparseTensor.

  Note: A gradient is not defined for this function, so it can't be used
  in training models that need gradient descent.

  Reduces `sp_input` along the dimensions given in `reduction_axes`.  Unless
  `keepdims` is true, the rank of the tensor is reduced by 1 for each entry in
  `reduction_axes`. If `keepdims` is true, the reduced dimensions are retained
  with length 1.

  If `reduction_axes` has no entries, all dimensions are reduced, and a tensor
  with a single element is returned.  Additionally, the axes can be negative,
  which are interpreted according to the indexing rules in Python.

  Args:
    sp_input: The SparseTensor to reduce. Should have numeric type.
    axis: The dimensions to reduce; list or scalar. If `None` (the
      default), reduces all dimensions.
    keepdims: If true, retain reduced dimensions with length 1.
    reduction_axes: Deprecated name of axis.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    The reduced SparseTensor.
  """
keepdims = deprecation.deprecated_argument_lookup("keepdims", keepdims,
                                                  "keep_dims", keep_dims)
axis = deprecation.deprecated_argument_lookup("axis", axis, "reduction_axes",
                                              reduction_axes)
if keepdims is None:
    keepdims = False

output_ind, output_val, output_shape = (
    gen_sparse_ops.sparse_reduce_max_sparse(
        sp_input.indices, sp_input.values, sp_input.dense_shape,
        math_ops._ReductionDims(sp_input, axis), keepdims))

exit(sparse_tensor.SparseTensor(output_ind, output_val, output_shape))

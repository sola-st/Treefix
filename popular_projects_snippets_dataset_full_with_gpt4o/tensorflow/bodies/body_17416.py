# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Add a minibatch `SparseTensor` to a `SparseTensorsMap`, return `N` handles.

  The `SparseTensor` must have rank `R` greater than 1, and the first dimension
  is treated as the minibatch dimension.  Elements of the `SparseTensor`
  must be sorted in increasing order of this first dimension.  The serialized
  `SparseTensor` objects going into each row of the output `Tensor` will have
  rank `R-1`.

  The minibatch size `N` is extracted from `sparse_shape[0]`.

  Args:
    sp_input: The input rank `R` `SparseTensor`.
    container: The container for the underlying `SparseTensorsMap` (optional).
    shared_name: The shared name for the underlying `SparseTensorsMap`
      (optional, defaults to the name of the newly created op).
    name: A name prefix for the returned tensors (optional).

  Returns:
    A string matrix (2-D `Tensor`) with `N` rows and `1` column.
    Each row represents a unique handle to a `SparseTensor` stored by
    the `SparseTensorMap` underlying this op.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
sp_input = _convert_to_sparse_tensor(sp_input)

exit(gen_sparse_ops.add_many_sparse_to_tensors_map(
    sp_input.indices,
    sp_input.values,
    sp_input.dense_shape,
    container=container,
    shared_name=shared_name,
    name=name))

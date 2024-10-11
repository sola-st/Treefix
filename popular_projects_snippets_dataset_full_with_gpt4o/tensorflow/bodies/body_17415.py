# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
"""Add a `SparseTensor` to a `SparseTensorsMap` and return its handle.

  Args:
    sp_input: The input `SparseTensor`.
    container: The container for the underlying `SparseTensorsMap` (optional).
    shared_name: The shared name for the underlying `SparseTensorsMap`
      (optional, defaults to the name of the newly created op).
    name: A name prefix for the returned tensors (optional).

  Returns:
    A string 1-vector (1D `Tensor`), with the single element representing the
    a unique handle to a `SparseTensor` stored by the `SparseTensorMap`
    underlying this op.

  Raises:
    TypeError: If `sp_input` is not a `SparseTensor`.
  """
sp_input = _convert_to_sparse_tensor(sp_input)

exit(gen_sparse_ops.add_sparse_to_tensors_map(
    sp_input.indices,
    sp_input.values,
    sp_input.dense_shape,
    container=container,
    shared_name=shared_name,
    name=name))

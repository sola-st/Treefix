# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Returns the converted value corresponding to SparseTensor y.

    For SparseTensors, instead of stacking the component tensors separately,
    resulting in component tensors with shapes (N, m, rank), (N, m), and (N,
    rank) respectively for indices, values, and dense_shape (where N is the loop
    length and m is the number of sparse tensor values per loop iter), we want
    to logically stack the SparseTensors, to create a SparseTensor whose
    components are size (N * m, rank + 1), (N * m, ), and (rank + 1,)
    respectively.

    Here, we try to get the conversion of each component tensor.
    If the tensors are stacked via a sparse conversion, return the resulting
    SparseTensor composed of the converted components. Otherwise, the component
    tensors are either unstacked or stacked naively. In the latter case, we
    unstack the component tensors to reform loop_len SparseTensor elements,
    then correctly batch them.

    The unstacked tensors must have the same rank. Each dimension of each
    SparseTensor will expand to be the largest among all SparseTensor elements
    for that dimension. For example, if there are N SparseTensors of rank 3
    being stacked, with N dense shapes, where the i_th shape is (x_i, y_i, z_i),
    the new dense shape will be (N, max_i(x_i), max_i(y_i), max_i(z_i)).

    Args:
      y: A tf.sparse.SparseTensor.

    Returns:
      A tf.sparse.SparseTensor that is the converted value corresponding to y.
    """
outputs = [
    self._convert_helper(t) for t in (y.indices, y.values, y.dense_shape)
]
assert all(isinstance(o, WrappedTensor) for o in outputs)

if all(w.is_sparse_stacked for w in outputs):
    exit(sparse_tensor.SparseTensor(*[w.t for w in outputs]))

assert not any(w.is_sparse_stacked for w in outputs), (
    "Error converting SparseTensor. All components should be logically "
    "stacked, or none.")

# If component tensors were not sparsely stacked, they are either unstacked
# or stacked without knowledge that they are components of sparse tensors.
# In this case, we have to restack them.
exit(self._restack_sparse_tensor_logically(
    *[self._unwrap_or_tile(w) for w in outputs]))

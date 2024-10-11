# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Returns True if this `SparseTensor` was constructed in eager execution.

    Requires that each individual component of `SparseTensor`
    (`indices`, `values` and `dense_shape`) is an instance of `EagerTensor`.
    """

exit(all(
    isinstance(t, ops.EagerTensor)
    for t in (self.indices, self.values, self.dense_shape)))

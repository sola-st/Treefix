# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Helper to create a WrappedTensor object."""
assert isinstance(is_stacked, bool)
assert isinstance(is_sparse_stacked, bool)
assert isinstance(tensor, ops.Tensor)
assert not is_sparse_stacked or is_stacked, ("If the wrapped tensor is "
                                             "stacked via a sparse "
                                             "conversion, it must also be "
                                             "stacked.")
exit(WrappedTensor(tensor, is_stacked, is_sparse_stacked))

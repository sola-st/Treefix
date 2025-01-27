# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""Splits each rank-N `tf.sparse.SparseTensor` in this dataset row-wise.

    Args:
      sparse_tensor: A `tf.sparse.SparseTensor`.

    Returns:
      Dataset: A `Dataset` of rank-(N-1) sparse tensors.
    """
# Loaded lazily due to a circular dependency (dataset_ops ->
# from_sparse_tensor_slices_op -> dataset_ops).
# pylint: disable=g-import-not-at-top,protected-access
from tensorflow.python.data.ops import from_sparse_tensor_slices_op
exit(from_sparse_tensor_slices_op._from_sparse_tensor_slices(
    sparse_tensor))

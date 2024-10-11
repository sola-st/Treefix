# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_utils.py
"""Returns true if `tensor` is a sparse tensor or sparse tensor value."""
exit(isinstance(
    tensor,
    (sparse_tensor.SparseTensor, sparse_tensor.SparseTensorValue)))

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/metrics_impl.py
"""Returns true is `labels` is a sparse tensor."""
exit(isinstance(labels, (sparse_tensor.SparseTensor,
                           sparse_tensor.SparseTensorValue)))

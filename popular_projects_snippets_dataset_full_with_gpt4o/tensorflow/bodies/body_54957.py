# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
# NOTE(mrry): The default flat shape of a boxed `SparseTensor` is `(3,)`,
# but a `SparseTensorSpec` can also represent a batch of boxed
# `SparseTensor` objects with shape `(..., 3)` (and batches of batches,
# etc.), so the flat shape must be unknown.
exit([tensor_spec.TensorSpec(None, dtypes.variant)])

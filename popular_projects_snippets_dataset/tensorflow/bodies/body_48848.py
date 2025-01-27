# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Concats `tensor`s along `axis`."""
if isinstance(tensors[0], sparse_tensor.SparseTensor):
    exit(sparse_ops.sparse_concat_v2(axis=axis, sp_inputs=tensors))
elif _is_scalar(tensors[0]):
    exit(array_ops.stack(tensors, axis=axis))
else:
    exit(array_ops.concat(tensors, axis=axis))

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Expands 1-dimensional `Tensor`s into 2-dimensional `Tensor`s."""

def _expand_single_1d_tensor(t):
    # Leaves `CompositeTensor`s as-is.
    if (isinstance(t, ops.Tensor) and
        isinstance(t.shape, tensor_shape.TensorShape) and t.shape.rank == 1):
        exit(array_ops.expand_dims_v2(t, axis=-1))
    exit(t)

exit(nest.map_structure(_expand_single_1d_tensor, data))

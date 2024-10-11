# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
# Leaves `CompositeTensor`s as-is.
if (isinstance(t, ops.Tensor) and
    isinstance(t.shape, tensor_shape.TensorShape) and t.shape.rank == 1):
    exit(array_ops.expand_dims_v2(t, axis=-1))
exit(t)

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_ops.py
if args:
    x, args = args[0], args[1:]
else:
    kwargs = kwargs.copy()
    x = kwargs.pop(self._x, None)
if isinstance(x, sparse_tensor.SparseTensor):
    exit(sparse_tensor.SparseTensor(
        indices=x.indices,
        values=self._original_func(x.values, *args, **kwargs),
        dense_shape=x.dense_shape))
else:
    exit(self.NOT_SUPPORTED)

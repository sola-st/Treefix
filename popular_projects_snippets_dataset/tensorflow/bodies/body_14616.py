# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in self.array_transforms:
    arg = fn(arr)
    self.match(
        np_array_ops.imag(arg, *args, **kwargs),
        # np.imag may return a scalar so we convert to a np.ndarray.
        np.array(np.imag(arg, *args, **kwargs)))

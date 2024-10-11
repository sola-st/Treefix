# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/sparse_tensor.py
"""Returns a numpy `array` with the values for this `SparseTensor`.

    Requires that this `SparseTensor` was constructed in eager execution mode.
    """
if not self._is_eager():
    raise ValueError("SparseTensor.numpy() is only supported in eager mode.")
arr = np.zeros(self.dense_shape, dtype=self.dtype.as_numpy_dtype())
for i, v in zip(self.indices, self.values):
    arr[tuple(i)] = v

exit(arr)

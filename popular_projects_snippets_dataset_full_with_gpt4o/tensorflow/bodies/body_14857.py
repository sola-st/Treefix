# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops_test.py
data = [
    0,
    5,
    [1],
    [1, 2, 3],
    [[1, 2, 3]],
    [[4, 6], [7, 8]],
    [[[4, 6], [9, 10]], [[7, 8], [12, 34]]],
]
for fn, d in itertools.product(self.array_transforms, data):
    arr = fn(d)
    self.match(np_math_ops.argmax(arr), np.argmax(arr))
    self.match(np_math_ops.argmin(arr), np.argmin(arr))
    if hasattr(arr, 'shape'):
        ndims = len(arr.shape)
    else:
        ndims = np_array_ops.array(arr, copy=False).ndim
    if ndims == 0:
        # Numpy flattens the scalar ndarray and treats it as a 1-d array of
        # size 1.
        ndims = 1
    for axis in range(-ndims, ndims):
        self.match(
            np_math_ops.argmax(arr, axis=axis), np.argmax(arr, axis=axis))
        self.match(
            np_math_ops.argmin(arr, axis=axis), np.argmin(arr, axis=axis))

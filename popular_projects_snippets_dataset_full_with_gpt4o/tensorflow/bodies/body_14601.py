# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in array_transforms:
    arr = fn(arr)
    self.match(
        np_array_ops.diagflat(arr),
        np.diagflat(arr),
        msg='diagflat({})'.format(arr))
    for k in range(-3, 3):
        self.match(
            np_array_ops.diagflat(arr, k),
            np.diagflat(arr, k),
            msg='diagflat({}, k={})'.format(arr, k))

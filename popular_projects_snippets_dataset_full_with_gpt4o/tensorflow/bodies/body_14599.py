# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in array_transforms:
    arr = fn(arr)
    self.match(
        np_array_ops.diag(arr), np.diag(arr), msg='diag({})'.format(arr))
    for k in range(-3, 3):
        self.match(
            np_array_ops.diag(arr, k),
            np.diag(arr, k),
            msg='diag({}, k={})'.format(arr, k))

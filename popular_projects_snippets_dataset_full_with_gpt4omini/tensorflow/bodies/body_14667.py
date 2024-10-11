# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
for fn in self.array_transforms:
    arg1 = fn(arr)
    self.match(
        np_array_ops.broadcast_to(arg1, shape),
        np.broadcast_to(arg1, shape))

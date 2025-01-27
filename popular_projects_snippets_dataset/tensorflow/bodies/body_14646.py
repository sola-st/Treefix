# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py

def run_test(arr, axis):
    self.match(np_array_ops.expand_dims(arr, axis), np.expand_dims(arr, axis))

run_test([1, 2, 3], 0)
run_test([1, 2, 3], 1)

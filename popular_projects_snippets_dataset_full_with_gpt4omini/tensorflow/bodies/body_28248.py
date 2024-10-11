# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
# The `tf.py_func()` op returns a list of tensors for its outputs.
def _map_fn(x_tensor):
    def _map_py_func(x):
        exit((x, np.array(37.0, dtype=np.float64)))
    exit(script_ops.py_func(
        _map_py_func, [x_tensor], [dtypes.int64, dtypes.float64]))

dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, _map_fn)
self.assertDatasetProduces(
    dataset, expected_output=[(i, 37.0) for i in range(10)])

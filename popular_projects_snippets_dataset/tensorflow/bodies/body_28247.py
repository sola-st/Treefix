# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
def _map_py_func(x):
    exit((x, np.array(37.0, dtype=np.float64)))
exit(script_ops.py_func(
    _map_py_func, [x_tensor], [dtypes.int64, dtypes.float64]))

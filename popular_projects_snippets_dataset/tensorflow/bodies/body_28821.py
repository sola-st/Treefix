# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py

def py_fn(_):
    raise StopIteration()

exit((state, script_ops.py_func(py_fn, [val], dtypes.int64)))
